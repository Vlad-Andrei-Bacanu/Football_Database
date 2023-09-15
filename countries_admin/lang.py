class WikipediaLanguage:

    def __init__(self, name : str, subdomain : str):
        self.name = str(name)
        self.subdomain = str(subdomain)



LANGUAGES = {
    'ABK' : WikipediaLanguage('Abkhazian', 'ab'),
    'ACH' : WikipediaLanguage('Acehnese', 'ace'),
    'ADG' : WikipediaLanguage('Adyghe', 'ady'),
    'AFR' : WikipediaLanguage('Afrikaans', 'af'),
    'ALB' : WikipediaLanguage('Albanian', 'sq'),
    'ALM' : WikipediaLanguage('Alemannic', 'als'),
    'AMH' : WikipediaLanguage('Amharic', 'am'),
    'AMS' : WikipediaLanguage('Amis', 'ami'),
    'ANG' : WikipediaLanguage('Angika', 'anp'),
    'ARB' : WikipediaLanguage('Arabic', 'ar'),
    'ARG' : WikipediaLanguage('Aragonese', 'an'),
    'AMC' : WikipediaLanguage('Aramaic', 'arc'),
    'ARM' : WikipediaLanguage('Armenian', 'hy'),
    'ARO' : WikipediaLanguage('Aromanian', 'roa-rup'),
    'ARP' : WikipediaLanguage('Arpitan', 'arp'),
    'ASS' : WikipediaLanguage('Assamese', 'as'),
    'AST' : WikipediaLanguage('Asturian', 'ast'),
    'ATK' : WikipediaLanguage('Atikamekw', 'atj'),
    'AVR' : WikipediaLanguage('Avaric', 'av'),
    'AWD' : WikipediaLanguage('Awadhi', 'awa'),
    'AYM' : WikipediaLanguage('Aymara', 'ay'),
    'AZE' : WikipediaLanguage('Azerbaijani', 'az'),
    'BAL' : WikipediaLanguage('Balinese', 'ban'),
    'BAM' : WikipediaLanguage('Bambara', 'bm'),
    'BNG' : WikipediaLanguage('Bengali', 'bn'),
    'BNJ' : WikipediaLanguage('Banjar', 'bjn'),
    'BSB' : WikipediaLanguage('Basa Banyumasan', 'map-bms'),
    'BSK' : WikipediaLanguage('Bashkir', 'ba'),
    'BSQ' : WikipediaLanguage('Basque', 'eu'),
    'BAV' : WikipediaLanguage('Bavarian', 'bar'),
    'BLR' : WikipediaLanguage('Belarusian', 'be'),
    'BHO' : WikipediaLanguage('Bhojpuri', 'bh'),
    'BSH' : WikipediaLanguage('Bishnupriya', 'bpy'),
    'BIS' : WikipediaLanguage('Bislama', 'bi'),
    'BIH' : WikipediaLanguage('Bosnian', 'bs'),
    'BRE' : WikipediaLanguage('Breton', 'br'),
    'BUG' : WikipediaLanguage('Buginese', 'bug'),
    'BUL' : WikipediaLanguage('Bulgarian', 'bg'),
    'BUR' : WikipediaLanguage('Burmese', 'my'),
    'CAN' : WikipediaLanguage('Cantonese', 'zh-yue'),
    'CAT' : WikipediaLanguage('Catalan', 'ca'),
    'CEB' : WikipediaLanguage('Cebuano', 'ceb'),
    'CBK' : WikipediaLanguage('Central Bikol', 'bcl'),
    'CKD' : WikipediaLanguage('Central Kurdish', 'ckb'),
    'CHM' : WikipediaLanguage('Chamorro', 'ch'),
    'CHV' : WikipediaLanguage('Chavacano', 'cbk-zam'),
    'CHE' : WikipediaLanguage('Chechen', 'ce'),
    'CHR' : WikipediaLanguage('Cherokee', 'chr'),
    'CHY' : WikipediaLanguage('Cheyenne', 'chy'),
    'CHN' : WikipediaLanguage('Chinese', 'zh'),
    'CSL' : WikipediaLanguage('Church Slavic', 'cu'),
    'CHU' : WikipediaLanguage('Chuvash', 'cv'),
    'CLG' : WikipediaLanguage('Colognian', 'ksh'),
    'COR' : WikipediaLanguage('Cornish', 'kw'),
    'CRS' : WikipediaLanguage('Corsican', 'co'),
    'CRE' : WikipediaLanguage('Cree', 'cr'),
    'CRT' : WikipediaLanguage('Crimean Tatar', 'crh'),
    'CRO' : WikipediaLanguage('Croatian', 'hr'),
    'CZE' : WikipediaLanguage('Czech', 'cs'),
    'DAG' : WikipediaLanguage('Dagbani', 'dag'),
    'DEN' : WikipediaLanguage('Danish', 'da'),
    'DIN' : WikipediaLanguage('Dinka', 'din'),
    'DHV' : WikipediaLanguage('Dhivehi', 'dv'),
    'DOT' : WikipediaLanguage('Doteli', 'dty'),
    'DUT' : WikipediaLanguage('Dutch', 'nl'),
    'DZG' : WikipediaLanguage('Dzongkha', 'dz'),
    'EMR' : WikipediaLanguage('Eastern Mari', ''),
    'EGY' : WikipediaLanguage('Egyptian Arabic', ''),
    'ERO' : WikipediaLanguage('Emiliano-Romagnolo', ''),
    'ENG' : WikipediaLanguage('English', ''),
    'ERZ' : WikipediaLanguage('Erzya', ''),
    'ESR' : WikipediaLanguage('Esperanto', ''),
    'EST' : WikipediaLanguage('Estonian', ''),
    'EWE' : WikipediaLanguage('Ewe', ''),
    'EXT' : WikipediaLanguage('Extremaduran', ''),
    'FAN' : WikipediaLanguage('Fanti', ''),
    'FAR' : WikipediaLanguage('Faroese', ''),
    'FIJ' : WikipediaLanguage('Fijian', ''),
    'FIN' : WikipediaLanguage('Finnish', ''),
    'FRF' : WikipediaLanguage('Frafra', ''),
    'FRA' : WikipediaLanguage('French', ''),
    'FRI' : WikipediaLanguage('Friulian', ''),
    'FUL' : WikipediaLanguage('Fula', ''),
    'GGZ' : WikipediaLanguage('Gagauz', ''),
    'GAL' : WikipediaLanguage('Galician', ''),
    'GAN' : WikipediaLanguage('Gan Chinese', ''),
    'GAD' : WikipediaLanguage('Ganda', ''),
    'GEO' : WikipediaLanguage('Georgian', ''),
    'GER' : WikipediaLanguage('German', ''),
    'GHA' : WikipediaLanguage('Ghanaian Pidgin', ''),
    'GIL' : WikipediaLanguage('Gilaki', ''),
    'GOK' : WikipediaLanguage('Goan Konkani', ''),
    'GOR' : WikipediaLanguage('Gotontalo', ''),
    'GOT' : WikipediaLanguage('Gothic', ''),
    'GRE' : WikipediaLanguage('Greek', ''),
    'GUA' : WikipediaLanguage('Guarani', ''),
    'GUI' : WikipediaLanguage('Guianan Creole', ''),
    'GUJ' : WikipediaLanguage('Gujarati', ''),
    'GUN' : WikipediaLanguage('Gun', ''),
    'HTI' : WikipediaLanguage('Haitian Creole', ''),
    'HKC' : WikipediaLanguage('Hakka Chinese', ''),
    'HAU' : WikipediaLanguage('Hausa', ''),
    'HAW' : WikipediaLanguage('Hawaiian', ''),
    'HEB' : WikipediaLanguage('Hebrew', ''),
    'HIN' : WikipediaLanguage('Hindi', ''),
    'HUN' : WikipediaLanguage('Hungarian', ''),
    'ISL' : WikipediaLanguage('Icelandic', ''),
    'IDO' : WikipediaLanguage('Ido', ''),
    'IGB' : WikipediaLanguage('Igbo', ''),
    'ILO' : WikipediaLanguage('Iloko', ''),
    'INS' : WikipediaLanguage('Inari Sami', ''),
    'IDN' : WikipediaLanguage('Indonesian', ''),
    'ING' : WikipediaLanguage('Ingush', ''),
    'INU' : WikipediaLanguage('Inuktitut', ''),
    'INP' : WikipediaLanguage('Inupiaq', ''),
    'IRL' : WikipediaLanguage('Irish', ''),
    'ITA' : WikipediaLanguage('Italian', ''),
    'JAM' : WikipediaLanguage('Jamaican Creole English', ''),
    'JPN' : WikipediaLanguage('Japanese', ''),
    'JAV' : WikipediaLanguage('Javanese', ''),
    'KAB' : WikipediaLanguage('Kabardian', ''),
    'KBY' : WikipediaLanguage('Kabyle', ''),
    'KLA' : WikipediaLanguage('Kalaallisut', ''),
    'KAL' : WikipediaLanguage('Kalmyk', ''),
    'KAN' : WikipediaLanguage('Kannada', ''),
    'KRK' : WikipediaLanguage('Kara-Kalpak', ''),
    'KRB' : WikipediaLanguage('Karachay-Balkar', ''),
    'KSH' : WikipediaLanguage('Kashmiri', ''),
    'KSB' : WikipediaLanguage('Kashubian', ''),
    'KAZ' : WikipediaLanguage('Kazakh', ''),
    'KHM' : WikipediaLanguage('Khmer', ''),
    'KIK' : WikipediaLanguage('Kikuyu', ''),
    'KIN' : WikipediaLanguage('Kinyarwanda', ''),
    'KOM' : WikipediaLanguage('Komi', ''),
    'KOP' : WikipediaLanguage('Komi-Permyak', ''),
    'KON' : WikipediaLanguage('Kongo', ''),
    'KOR' : WikipediaLanguage('Korean', ''),
    'KOT' : WikipediaLanguage('Kotava', ''),
    'KUR' : WikipediaLanguage('Kurdish', ''),
    'KYG' : WikipediaLanguage('Kyrgyz', ''),
    'LAD' : WikipediaLanguage('Ladin', ''),
    'LDO' : WikipediaLanguage('Ladino', ''),
    'LAK' : WikipediaLanguage('Lak', ''),
    'LAO' : WikipediaLanguage('Lao', ''),
    'LTG' : WikipediaLanguage('Latgalian', ''),
    'LAT' : WikipediaLanguage('Latin', ''),
    'LVA' : WikipediaLanguage('Latvian', ''),
    'LEZ' : WikipediaLanguage('Lezghian', ''),
    'LIG' : WikipediaLanguage('Ligurian', ''),
    'LIM' : WikipediaLanguage('Limburgish', ''),
    'LIN' : WikipediaLanguage('Lingala', ''),
    'LTU' : WikipediaLanguage('Lithuanian', ''),
    'LVK' : WikipediaLanguage('Livvi-Karelian', ''),
    'LOJ' : WikipediaLanguage('Lojban', ''),
    'LOM' : WikipediaLanguage('Lombard', ''),
    'LGE' : WikipediaLanguage('Low German', ''),
    'LSX' : WikipediaLanguage('Low Saxon', ''),
    'LSO' : WikipediaLanguage('Lower Sorbian', ''),
    'LUX' : WikipediaLanguage('Luxembourgish', ''),
    'MKD' : WikipediaLanguage('Macedonian', ''),
    'MAD' : WikipediaLanguage('Madurese', ''),
    'MAI' : WikipediaLanguage('Maithili', ''),
    'MLG' : WikipediaLanguage('Malagasy', ''),
    'MAL' : WikipediaLanguage('Malay', ''),
    'MLY' : WikipediaLanguage('Malayalam', ''),
    'MLT' : WikipediaLanguage('Maltese', ''),
    'MNP' : WikipediaLanguage('Manipuri', ''),
    'MAX' : WikipediaLanguage('Manx', ''),
    'MAO' : WikipediaLanguage('Maori', ''),
    'MTH' : WikipediaLanguage('Marathi', ''),
    'MAZ' : WikipediaLanguage('Mazanderani', ''),
    'MDC' : WikipediaLanguage('Min Dong Chinese', ''),
    'MNC' : WikipediaLanguage('Min Nan Chinese', ''),
    'MNK' : WikipediaLanguage('Minangkabau', ''),
    'MIG' : WikipediaLanguage('Mingrelian', ''),
    'MIR' : WikipediaLanguage('Mirandese', ''),
    'MOK' : WikipediaLanguage('Moksha', ''),
    'MON' : WikipediaLanguage('Mon', ''),
    'MGL' : WikipediaLanguage('Mongolian', ''),
    'MAR' : WikipediaLanguage('Moroccan Arabic', ''),
    'NKO' : WikipediaLanguage('N\'Ko', ''),
    'NAH' : WikipediaLanguage('Nahuatl', ''),
    'NAV' : WikipediaLanguage('Navajo', ''),
    'NAP' : WikipediaLanguage('Neapolitan', ''),
    'NPL' : WikipediaLanguage('Nepali', ''),
    'NEW' : WikipediaLanguage('Newari', ''),
    'NIA' : WikipediaLanguage('Nias', ''),
    'NGA' : WikipediaLanguage('Nigerian Pidgin', ''),
    'NPT' : WikipediaLanguage('Norfuk/Pitkern', ''),
    'NRM' : WikipediaLanguage('Norman', ''),
    'NFR' : WikipediaLanguage('Northern Frisian', ''),
    'NSA' : WikipediaLanguage('Northern Sami', ''),
    'NSO' : WikipediaLanguage('Northern Sotho', ''),
    'NOR' : WikipediaLanguage('Norwegian', ''),
    'NNY' : WikipediaLanguage('Norwegian Nynorsk', ''),
    'NOV' : WikipediaLanguage('Novial', ''),
    'NYA' : WikipediaLanguage('Nyanja', ''),
    'OCC' : WikipediaLanguage('Occitan', ''),
    'ODI' : WikipediaLanguage('Odia', ''),
    'OEN' : WikipediaLanguage('Old English', ''),
    'ORO' : WikipediaLanguage('Oromo', ''),
    'OSS' : WikipediaLanguage('Ossetic', ''),
    'PAO' : WikipediaLanguage('Pa\'O', ''),
    'PAW' : WikipediaLanguage('Paiwan', ''),
    'PGE' : WikipediaLanguage('Palatine German', ''),
    'PAL' : WikipediaLanguage('Pali', ''),
    'PMP' : WikipediaLanguage('Pampanga', ''),
    'PAN' : WikipediaLanguage('Pangasinan', ''),
    'PAP' : WikipediaLanguage('Papiamento', ''),
    'PSH' : WikipediaLanguage('Pashto', ''),
    'PEG' : WikipediaLanguage('Pennsylvania German', ''),
    'PER' : WikipediaLanguage('Persian', ''),
    'PIC' : WikipediaLanguage('Picard', ''),
    'PID' : WikipediaLanguage('Piedmontese', ''),
    'POL' : WikipediaLanguage('Polish', ''),
    'PON' : WikipediaLanguage('Pontic', ''),
    'POR' : WikipediaLanguage('Portuguese', ''),
    'PUN' : WikipediaLanguage('Punjabi', ''),
    'QUE' : WikipediaLanguage('Quechua', ''),
    'ROU' : WikipediaLanguage('Romanian', ''),
    'ROM' : WikipediaLanguage('Romansh', ''),
    'RUN' : WikipediaLanguage('Rundi', ''),
    'RUB' : WikipediaLanguage('Russia Buriat', ''),
    'RUS' : WikipediaLanguage('Russian', ''),
    'RSN' : WikipediaLanguage('Rusyn', ''),
    'SAK' : WikipediaLanguage('Sakizaya', ''),
    'SAM' : WikipediaLanguage('Samoan', ''),
    'SMG' : WikipediaLanguage('Samogitian', ''),
    'SAN' : WikipediaLanguage('Sango', ''),
    'SNS' : WikipediaLanguage('Sanskrit', ''),
    'SAT' : WikipediaLanguage('Santali', ''),
    'SAR' : WikipediaLanguage('Saraiki', ''),
    'SRD' : WikipediaLanguage('Sardinian', ''),
    'SFR' : WikipediaLanguage('Saterland Frisian', ''),
    'SCO' : WikipediaLanguage('Scots', ''),
    'SCG' : WikipediaLanguage('Scottish Gaelic', ''),
    'SRB' : WikipediaLanguage('Serbian', ''),
    'SRC' : WikipediaLanguage('Serbo-Croatian', ''),
    'SHA' : WikipediaLanguage('Shan', ''),
    'SHN' : WikipediaLanguage('Shona', ''),
    'SIC' : WikipediaLanguage('Sicilian', ''),
    'SIL' : WikipediaLanguage('Silesian', ''),
    'SEN' : WikipediaLanguage('Simple English', ''),
    'SND' : WikipediaLanguage('Sindhi', ''),
    'SNH' : WikipediaLanguage('Sinhala', ''),
    'SVK' : WikipediaLanguage('Slovak', ''),
    'SVN' : WikipediaLanguage('Slovenian', ''),
    'SOM' : WikipediaLanguage('Somali', ''),
    'SAZ' : WikipediaLanguage('South Azerbaijani', ''),
    'SAL' : WikipediaLanguage('Southern Altai', ''),
    'SSO' : WikipediaLanguage('Southern Sotho', ''),
    'ESP' : WikipediaLanguage('Spanish', ''),
    'SRT' : WikipediaLanguage('Sranan Tongo', ''),
    'SUN' : WikipediaLanguage('Sundanese', ''),
    'SWA' : WikipediaLanguage('Swahili', ''),
    'SWT' : WikipediaLanguage('Swati', ''),
    'SWE' : WikipediaLanguage('Swedish', ''),
    'TCH' : WikipediaLanguage('Tachelhit', ''),
    'TGL' : WikipediaLanguage('Tagalog', ''),
    'THT' : WikipediaLanguage('Tahitian', ''),
    'TJK' : WikipediaLanguage('Tajik', ''),
    'TAM' : WikipediaLanguage('Tamil', ''),
    'TAR' : WikipediaLanguage('Tarantino', ''),
    'TKO' : WikipediaLanguage('Taroko', ''),
    'TAT' : WikipediaLanguage('Tatar', ''),
    'TAY' : WikipediaLanguage('Tayal', ''),
    'TEL' : WikipediaLanguage('Telugu', ''),
    'TET' : WikipediaLanguage('Tetum', ''),
    'THA' : WikipediaLanguage('Thai', ''),
    'TIB' : WikipediaLanguage('Tibetan', ''),
    'TIG' : WikipediaLanguage('Tigrinya', ''),
    'TKP' : WikipediaLanguage('Tok Pisin', ''),
    'TGA' : WikipediaLanguage('Tongan', ''),
    'TSO' : WikipediaLanguage('Tsonga', ''),
    'TSW' : WikipediaLanguage('Tswana', ''),
    'TUL' : WikipediaLanguage('Tulu', ''),
    'TUM' : WikipediaLanguage('Tumbuka', ''),
    'TUR' : WikipediaLanguage('Turkish', ''),
    'TRK' : WikipediaLanguage('Turkmen', ''),
    'TUV' : WikipediaLanguage('Tuvinian', ''),
    'TWI' : WikipediaLanguage('Twi', ''),
    'TYA' : WikipediaLanguage('Tyap', ''),
    'UDM' : WikipediaLanguage('Udmurt', ''),
    'UKR' : WikipediaLanguage('Ukrainian', ''),
    'USO' : WikipediaLanguage('Upper Sorbian', ''),
    'URD' : WikipediaLanguage('Urdu', ''),
    'UYG' : WikipediaLanguage('Uyghur', ''),
    'UZB' : WikipediaLanguage('Uzbek', ''),
    'VED' : WikipediaLanguage('Venda', ''),
    'VEN' : WikipediaLanguage('Venetian', ''),
    'VEP' : WikipediaLanguage('Veps', ''),
    'VIE' : WikipediaLanguage('Vietnamese', ''),
    'VRO' : WikipediaLanguage('Vlax Romani', ''),
    'VLP' : WikipediaLanguage('Volapuk', ''),
    'VOR' : WikipediaLanguage('Voro', ''),
    'WLN' : WikipediaLanguage('Walloon', ''),
    'WRY' : WikipediaLanguage('Waray', ''),
    'WAY' : WikipediaLanguage('Wayuu', ''),
    'WAL' : WikipediaLanguage('Welsh', ''),
    'WFL' : WikipediaLanguage('West Flemish', ''),
    'WAR' : WikipediaLanguage('Western Armenian', ''),
    'WFR' : WikipediaLanguage('Western Frisian', ''),
    'WMR' : WikipediaLanguage('Western Mari', ''),
    'WPU' : WikipediaLanguage('Western Punjabi', ''),
    'WOL' : WikipediaLanguage('Wolof', ''),
    'WUC' : WikipediaLanguage('Wu Chinese', ''),
    'XHO' : WikipediaLanguage('Xhosa', ''),
    'YAK' : WikipediaLanguage('Yakut', ''),
    'YID' : WikipediaLanguage('Yiddish', ''),
    'YOR' : WikipediaLanguage('Yoruba', ''),
    'ZAZ' : WikipediaLanguage('Zazaki', ''),
    'ZEE' : WikipediaLanguage('Zeelandic', ''),
    'ZHU' : WikipediaLanguage('Zhuang', ''),
    'ZUL' : WikipediaLanguage('Zulu', '')
}
