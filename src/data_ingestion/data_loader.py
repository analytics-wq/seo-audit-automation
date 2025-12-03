"""Main data loader for SEO data files."""
import pandas as pd
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class DataLoader:
    """Loads and validates data from various SEO tool exports."""

    def __init__(self, data_dir: Path):
        """Initialize data loader.

        Args:
            data_dir: Directory containing SEO data files
        """
        self.data_dir = Path(data_dir)
        self.loaded_data: Dict[str, pd.DataFrame] = {}
        self.tools_detected: List[str] = []

    def detect_file_type(self, file_path: Path) -> Optional[str]:
        """Detect the type of SEO tool from file structure.

        Args:
            file_path: Path to the data file

        Returns:
            Tool name or None if not recognized
        """
        try:
            # Try to read first few rows to detect tool type
            if file_path.suffix.lower() in ['.xlsx', '.xls']:
                # Check for multiple sheets (could be GA4, Ahrefs, etc.)
                xl_file = pd.ExcelFile(file_path)
                sheet_names = xl_file.sheet_names

                # GA4 detection
                if any('ga4' in name.lower() for name in sheet_names):
                    return 'GA4'

                # Ahrefs detection
                if any(name in sheet_names for name in ['Backlinks', 'Referring domains', 'Anchors']):
                    return 'Ahrefs'

                # Read first sheet to detect other tools
                df = pd.read_excel(file_path, sheet_name=0, nrows=5)

            elif file_path.suffix.lower() == '.csv':
                df = pd.read_csv(file_path, nrows=5)
            else:
                return None

            columns = [str(col).lower() for col in df.columns]

            # SEMrush detection
            if any('semrush' in col for col in columns) or \
               any(col in ['url', 'issue type', 'issue category'] for col in columns):
                return 'SEMrush'

            # Google Search Console detection
            if all(col in columns for col in ['queries', 'clicks', 'impressions', 'ctr', 'position']):
                return 'GSC'
            if all(col in columns for col in ['top queries', 'clicks', 'impressions']):
                return 'GSC'

            # Screaming Frog detection
            if 'address' in columns and 'status code' in columns and 'title 1' in columns:
                return 'Screaming Frog'

            # PageSpeed detection
            if any(col in columns for col in ['largest contentful paint', 'first input delay', 'cumulative layout shift']):
                return 'PageSpeed'

            logger.warning(f"Could not detect tool type for {file_path.name}")
            return None

        except Exception as e:
            logger.error(f"Error detecting file type for {file_path}: {e}")
            return None

    def load_file(self, file_path: Path, tool_type: Optional[str] = None) -> Optional[pd.DataFrame]:
        """Load a data file.

        Args:
            file_path: Path to the data file
            tool_type: Optional tool type (auto-detected if not provided)

        Returns:
            DataFrame or None if loading failed
        """
        try:
            if tool_type is None:
                tool_type = self.detect_file_type(file_path)

            if tool_type is None:
                logger.warning(f"Skipping unrecognized file: {file_path.name}")
                return None

            # Load based on file extension
            if file_path.suffix.lower() in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path)
            elif file_path.suffix.lower() == '.csv':
                df = pd.read_csv(file_path)
            else:
                logger.warning(f"Unsupported file format: {file_path.suffix}")
                return None

            logger.info(f"Loaded {tool_type} data from {file_path.name} ({len(df)} rows)")

            if tool_type not in self.tools_detected:
                self.tools_detected.append(tool_type)

            return df

        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            return None

    def load_all_files(self) -> Dict[str, pd.DataFrame]:
        """Load all data files from the data directory.

        Returns:
            Dictionary mapping tool types to DataFrames
        """
        if not self.data_dir.exists():
            logger.error(f"Data directory does not exist: {self.data_dir}")
            return {}

        data_files = list(self.data_dir.glob('*.csv')) + \
                     list(self.data_dir.glob('*.xlsx')) + \
                     list(self.data_dir.glob('*.xls'))

        logger.info(f"Found {len(data_files)} data files in {self.data_dir}")

        for file_path in data_files:
            tool_type = self.detect_file_type(file_path)
            if tool_type:
                df = self.load_file(file_path, tool_type)
                if df is not None:
                    # Store with tool type as key
                    key = f"{tool_type}_{file_path.stem}"
                    self.loaded_data[key] = df

        logger.info(f"Successfully loaded data from {len(self.loaded_data)} files")
        logger.info(f"Detected tools: {', '.join(self.tools_detected)}")

        return self.loaded_data

    def get_date_range(self) -> tuple[str, str]:
        """Calculate the date range across all loaded data.

        Returns:
            Tuple of (start_date, end_date) as formatted strings
        """
        min_date = None
        max_date = None

        for key, df in self.loaded_data.items():
            # Look for date columns
            date_cols = [col for col in df.columns if 'date' in str(col).lower()]

            for col in date_cols:
                try:
                    dates = pd.to_datetime(df[col], errors='coerce').dropna()
                    if len(dates) > 0:
                        col_min = dates.min()
                        col_max = dates.max()

                        if min_date is None or col_min < min_date:
                            min_date = col_min
                        if max_date is None or col_max > max_date:
                            max_date = col_max
                except:
                    continue

        if min_date and max_date:
            return (
                min_date.strftime('%d/%m/%Y'),
                max_date.strftime('%d/%m/%Y')
            )
        else:
            # Default to last 12 months
            end = datetime.now()
            start = datetime(end.year - 1, end.month, 1)
            return (
                start.strftime('%d/%m/%Y'),
                end.strftime('%d/%m/%Y')
            )

    def get_ga4_data(self) -> Optional[pd.DataFrame]:
        """Get GA4 data if available."""
        for key, df in self.loaded_data.items():
            if 'GA4' in key:
                return df
        return None

    def get_gsc_data(self) -> Optional[pd.DataFrame]:
        """Get Google Search Console data if available."""
        for key, df in self.loaded_data.items():
            if 'GSC' in key:
                return df
        return None

    def get_semrush_data(self) -> Optional[pd.DataFrame]:
        """Get SEMrush data if available."""
        for key, df in self.loaded_data.items():
            if 'SEMrush' in key:
                return df
        return None

    def get_ahrefs_data(self) -> Optional[pd.DataFrame]:
        """Get Ahrefs data if available."""
        for key, df in self.loaded_data.items():
            if 'Ahrefs' in key:
                return df
        return None

    def get_screaming_frog_data(self) -> Optional[pd.DataFrame]:
        """Get Screaming Frog data if available."""
        for key, df in self.loaded_data.items():
            if 'Screaming Frog' in key:
                return df
        return None

    def get_pagespeed_data(self) -> Optional[pd.DataFrame]:
        """Get PageSpeed data if available."""
        for key, df in self.loaded_data.items():
            if 'PageSpeed' in key:
                return df
        return None
