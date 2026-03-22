page_settings = {
    "003": {"speaker_name_window_threshold": 0.2},
    "004": {"speaker_name_window_threshold": 0.5},
    "005": {"speaker_name_window_threshold": 0.5},
    "007": {"speaker_name_window_threshold": 0.5},
    "008": {"speaker_name_window_threshold": 0.5},
    "030": {"speaker_name_window_threshold": 0.5},
    "041": {
        "speaker_name_window_threshold": 0.5,
    },
    "045": {"speaker_name_window_threshold": 0.5},
    "074": {
        "speaker_name_window_threshold": 0.1,
    },
    "080": {"speaker_name_window_threshold": 0.2},
    "101": {
        "speaker_name_window_threshold": 0.2,
    },
    "107": {
        "speaker_name_window_threshold": 0.2,
    },
    "130": {"speaker_name_window_threshold": 0.2},
    "152": {"speaker_name_window_threshold": 0.2},
    "190": {"speaker_name_window_threshold": 0.2},
}

# font names without prefix (e.g. 'ABCDEE+Verdana,Italic' -> 'Verdana,Italic')
italic_font_names = [
    "Arial-ItalicMT",
    "Arial-BoldItalicMT",
    "Helvetica-Oblique",
    "Calibri,Italic",
    "Verdana,Italic",
    "TimesNewRomanPS-BoldItalicMT",
    "TimesNewRomanPS-ItalicMT",
    "Arial,Italic",
    "MetaPlusBook-Italic",
    "Calibri,BoldItalic",
    "Times-Italic",
    "Helvetica,Italic",
    "Helvetica,BoldItalic",
    "Arial,BoldItalic",
    "Times-Italic",
    "Calibri-Italic",
    "Times-BoldItalic",
    "Times New Roman,BoldItalic",
    "SegoeUI-Italic",
    "Times New Roman,Italic",
    "Calibri-BoldItalic",
    "Verdana-BoldItalic",
    "Verdana-Italic",
    "Helvetica-Oblique",
    "Helvetica-BoldOblique",
    "Aptos,Italic",
]

# if any of these strings appear in a line, the line is ignored - case insensitive
ignore_line_markers = [
    "rocky-beach.com",
    "www.rocky-beach. com",
    "www. rocky-beach. com",
    "www. rocky-beach com",
    "www.rocky-beach.om",
    "Die drei ??? und der",
    "Die drei ??? und das",
    "Die drei ??? und die",
    "Die drei ??? -",
    "Die drei ???...",
]

replacements = {
    # Hyphens
    "‐": "-",
    "–": "-",
    "—": "-",
    # Quotes
    "‘": "'",
    "’": "'",
    "‚": "'",
    "“": '"',
    "”": '"',
    "„": '"',
    "´": "'",
    "`": "'",
    "«": '"',
    "»": '"',
    # Ellipsis
    "…": "...",
    # Whitespaces
    "": " ",
    "": " ",
    "": " ",
}
