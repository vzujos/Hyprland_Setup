Las apps con número están ordenadas por preferencia.

Las apps con guiones no están ordenadas y falta indagar o escoger.

Esta lista ya se encuentra revisada hasta la Metadata.

Esta es la fuente:
https://wiki.archlinux.org/title/List_of_applications
(falta revisar: internet)

## Programa para imagenes

**Image visors**:
1. imv
    - Para ejecutarlo, usar 
    `imv [path]`.
    - Para setearlo por defecto, usar: `xdg-mime default imv.desktop image/[formato]` **REVISAR**
    - Se agregaron windowrules.

**Image browsers**:
- nomacs
- gThumb  

**Image editors**:
1. Pinta, Krita
2. GIMP
3. Mypaint [lienzo infinito]


## Programa para audios 

**Audio Players**:
- Sayonara — Small, clear and fast audio player for Linux written in C++, uses the Qt framework.
- Tauon Music Box — Modern, comfortable and streamlined music player for the playback of your music collection.
- DeaDBeeF — Light and fast music player with many features, no GNOME or KDE dependencies, supports console-only, as well as a GTK GUI, comes with many plugins, and has a metadata editor.

**Music tag editors**:
- Kid3 — MP3, Ogg/Vorbis, FLAC, MPC, MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV and AIFF files tag editor.
- Puddletag — Replacement for the famous MP3tag for Windows.

**Audio converters**:
- Flacon — Extracts individual tracks from one big audio file containing the entire album of music and saves them as separate audio files.
- soundKonverter — Qt-based GUI front-end to various audio converters.

**Audio editors**:
1. Audacity — Program that lets you manipulate digital audio waveforms.
2. oceanaudio — Propietary cross-platform, easy to use, fast and functional audio editor.

**Audio analyzers**:
- Friture — Real-time audio analyzer.
- Sonic Visualiser — Viewing, analyzing, and annotating the contents of music audio files.
- Spek — A barebones interface for ffmpeg's spectogram png output, helps to analyse your audio files by showing their spectrogram.
- FMIT — Graphical utility for tuning your musical instruments, with error and volume history and advanced features.
- SongRec — Unofficial Shazam client to recognize audio from an arbitrary audio file or from the microphone, written in Rust.

**Audio visualizers**:
- C.A.V.A. — Console-based audio visualizer for ALSA, MPD and PulseAudio.
- vibe — WGPU audio spectrum visualizer. Its primary use case is for desktop windows or backgrounds on wayland.
- projectM — Music visualizer which uses 3D accelerated iterative image-based rendering.

**Music ScoreWriters**:
1. MuseScore — Create, playback, and print sheet music.

**Lyrics players**:
1. OSD Lyrics — Lyric show compatible with various media players.

**Volume control**:
1. wpctl
2. alsamixer — Soundcard mixer for ALSA soundcard driver, with ncurses interface.
- helvum
- Volnoti — A lightweight volume notification daemon for GNU/Linux and other POSIX operating systems.


## Programa para videos

**Video players**:
- Clapper — Media player built for the GNOME desktop environment using GTK4 toolkit and powered by GStreamer.
- Haruna Video Player — Qt/QML video player built on top of mpv.
- mpv — Very basic GUI for mpv.
- VLC media player — Middleweight video player with support for a wide variety of audio and video formats.

**Video editors**:
1. Kdenlive — Non-linear video editor designed for basic to semi-professional work. Part of kde-multimedia.
2. Shotcut — Shotcut is a free, open source, cross-platform video editor.
3. Flowblade — Multitrack non-linear video editor for Linux, designed to provide a fast, robust editing experience.
- Blender — Fully integrated 3D graphics creation suite with a built-in non-linear video editor.

**Camara web**:
- Webcamoid — Full featured webcam suite.
- Guvcview — Simple interface for capturing and viewing video from v4l2 devices.4
- Kamoso — Webcam recorder from KDE community. Part of kde-multimedia.
- cameractrls — Command line and graphical application for configuring v4l2 devices.
- v4l-utils — Provides a series of utilities for media devices.


# Document section

## Text editors
- dte — Small, easy to use editor with multi-tabbed interface, syntax highlighting, ctags navigation, etc.
- micro — Modern and intuitive terminal-based text editor, written in go and extensible through plugins.
- nano — Console text editor based on pico with on-screen key bindings help.
- Tilde — Intuitive text editor with Windows-like key bindings.

## Office suites
- Calligra — Actively developed fork of KOffice, the KDE office suite. It offers most of the features of OpenOffice. Part of kde-office.
- Google Docs — Cloud office solution by Google.
- LibreOffice — The office productivity suite compatible to the open and standardized ODF document format. Fork of OpenOffice, supported by The Document Foundation.
- OnlyOffice — Office suite that combines text, spreadsheet and presentation editors.
- SoftMaker FreeOffice — Complete, reliable, lightning-fast and Microsoft Office-compatible proprietary office suite with a word processor, spreadsheet, and presentation graphics software.
- WPS Office — Proprietary office productivity suite, previously known as Kingsoft Office.
- Yozo Office — Proprietary office suite, compatible with MS Office.

## PDF

**Viewers**:
- fbgs — Poor man's PostScript/pdf viewer for the linux framebuffer console.
- apvlv — Lightweight document viewer with Vim keybindings using GTK libraries. Supports PDF, DjVu, EPUB, HTML and TXT.
- Atril — Simple multi-page document viewer for MATE. Supports DjVu, DVI, EPS, EPUB, PDF, PostScript, TIFF, XPS and Comicbook.
- CorePDF — Simple lightweight PDF viewer based on Qt and poppler. Part of C-Suite.
- Emacs — See also pdf-tools for improved pdf support (emacs-pdf-tools-gitAUR) and the djvu package for djvu support.
- Evince — Document viewer for GNOME using GTK. Supports DjVu, DVI, EPS, PDF, PostScript, TIFF, XPS and Comicbook.
- GNOME Document Viewer — Document viewer for GNOME using GTK. Modern fork of evince, partly written in Rust. Supports PDF, DjVu, TIFF, and Comic Books archives (CBR, CBT, CBZ, CB7). Part of gnome.
- llpp — Very fast PDF reader based off of MuPDF, that supports continuous page scrolling, bookmarking, and text search through the whole document.
- MuPDF — Very fast EPUB, FictionBook, PDF, XPS and Comicbook viewer written in portable C. Features CJK font support and vim-like bindings.
- Okular — Universal document viewer for KDE. Supports CHM, Comicbook, DjVu, DVI, EPUB, FictionBook, Mobipocket, ODT, PDF, Plucker, PostScript, TIFF and XPS. Part of kde-graphics.
- pdfpc — Presenter console with multi-monitor support for PDF files.
- qpdfview — Tabbed document viewer. It uses Poppler for PDF support, libspectre for PS support, DjVuLibre for DjVu support, CUPS for printing support and the Qt toolkit for its interface.
- Sioyek — Lightweight PDF viewer based on MuPDF with features designed for viewing research papers and technical books, e.g., marking, bookmarking, highlighting, searchable command palette, jumping to references, and more.
- Xreader — Document viewer part of the X-Apps Project. Supports DjVu, DVI, EPUB, PDF, PostScript, TIFF, XPS, Comicbook.
- Zathura — Highly customizable and functional document viewer (plugin based). Supports PDF, DjVu, PostScript and Comicbook.

**Editors**:
    flpsed — A PostScript and PDF annotator, only supports text boxes.
    HandyOutliner for DjVu / PDF — Make easier and faster the process of creating bookmarks for DjVu and PDF documents.
    jPDF Tweak — Java Swing application that can combine, split, rotate, reorder, watermark, encrypt, sign, and otherwise tweak PDF files.
    Paper Clip — PDF document metadata editor to edit the title, author, keywords and more details.
    PDF Arranger — Helps merge or split pdf documents and rotate, crop and rearrange pages. It is a maintained fork of PDF-Shuffler.
    PDF Chain — GTK front-end for PDFtk, written in C++, supporting concatenation, burst, watermarks, attaching files and more.
    PdfJumbler — Simple tool to rearrange, merge, delete and rotate pages in PDF files.
    PDF Mix Tool — Qt front-end for PoDoFo, written in C++, supports splitting, merging, rotating and mixing PDF files.
    PDFsam — Open source application, written in Java, supports merging, splitting and rotating.
    PDF Slicer — Simple application to extract, merge, rotate and reorder pages of PDF documents.
    PDF Tricks — Simple, efficient application for small manipulations in PDF files using Ghostscript.
    Master PDF Editor — Functional proprietary PDF editor. Latest version free for non-commercial use. The -free package is outdated but lacks a watermark.
    PDF4QT — Open source PDF editor.
    PDF Studio — All-in-one proprietary PDF editor similar to Adobe Acrobat.
    Camelot — Camelot: PDF Table Extraction for Humans.
    mupdf-tools — Tools developed as part of MuPDF, contains mutool(1) and muraster.
    pdf2svg — Convert PDF files to SVG files.
    pdfcmd — Command-line tool to join, cut, reorder or merge PDF files.
    pdfcpu — Command-line tool to create and modify PDFs.
    pdf_extbook — Extract bookmarked PDF pages.
    pdfgrep — Commandline utility to search text in PDF files.
    pdfjam — Can be used to n-up, join, rotate and flip PDFs and arrange them into a format suitable for book binding.
    pdfminer.six — Community maintained fork of pdfminer, a text extraction tool for PDF documents.
    PDFtk — Simple tool for doing everyday things with PDF documents.
    QPDF — Content-preserving PDF transformation system.
    Stapler — Light alternative to PDFtk using the PyPDF2 library.
    Tabula — Tabula is a tool for liberating data tables trapped inside PDF files.
    Vector Slicer — Export multi-page PDFs from an SVG.
    verapdf — A purpose-built, open source, file-format validator covering all PDF/A and PDF/UA parts and conformance levels.
    wrt2pdf — A CLI tool to create a PDF out of a plain text file.
    
## E-book
- Arianna — An ebook reader and library management app supporting EPUB files. Part of kde-graphics.
- baca — console epub reader.
- Beseda — Accessible (for visually impaired) console ebook-reader that can speak TXT, FB2, ABW, [X]HTML, ODT, DOCX books and documents.
- Bookworm — Simple, focused e-book reader for Elementary OS with EPUB, PDF, Mobipocket and Comicbook support.
- Calibre — E-book library management application that can also edit EPUB files, convert between different formats and sync with a variety of e-book readers. Supported formats include CHM, Comicbook, DjVu, DOCX, EPUB, FictionBook, HTML, HTMLZ, Kindle, LIT, LRF, Mobipocket, ODT, PDF, PRC, PDB, PML, RB, RTF, SNB, TCR, TXT and TXTZ.
- Cool Reader — E-book viewer with many supported formats such as EPUB (non-DRM), FictionBook, TXT, RTF, HTML, CHM and TCR.
- FBReader — E-book viewer with many supported formats such as EPUB, FictionBook, HTML, plucker, PalmDoc, zTxt, TCR, CHM, RTF, OEB, Mobipocket (non-DRM) and TXT.
- Foliate — Simple and modern GTK eBook reader. Supports EPUB, Mobipocket, Kindle, FictionBook, and Comicbook formats.
- KOReader — An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices
- Lector — Qt based e-book reader with PDF, EPUB, Kindle, Mobipocket and Comicbook support.
- Sigil — WYSIWYG EPUB e-book editor.

Some PDF viewers like apvlv, Atril, MuPDF, Okular, Xreader, and Zathura also support the EPUB format. 

## Others
- Typst
- Zotero


# Otra seccion

## File managers
1. Dolphin
    - Con la opción de jpeg creo
2. Thunar
3. Nemo


---

## Metadata

- CoreInfo — Simple media metadata viewer built on mediainfo library. Part of C-Suite.
- DV Analyzer — Technical quality control and reporting tool that examines DV streams in order to report errors.
- ExifCleaner — Desktop app to clean metadata from images, videos, PDFs, and other files.
- ExifTool — Command-line application for reading, writing and editing meta information in a wide variety of files.
- Exiv2 — Command line utility to manage image metadata. It provides fast and easy read and write access to the Exif, IPTC and XMP metadata and the ICC Profile embedded within digital images in various formats.
- ffprobe — Gather information from multimedia streams and print it in human- and machine-readable fashion.
- jExifToolGUI — Java/Swing graphical frontend for ExifTool, which reads and writes all kind of metadata tags from/to image files.
- jhead — Exif jpeg header manipulation tool.
- mat2 — Metadata removal tool, supporting a wide range of commonly used file formats.
- MediaConch — Implementation checker, policy checker, reporter, and fixer.
- MediaInfo — Convenient unified display of the most relevant technical and tag data for video and audio files.
- sndfile-info — Obtaining information about the contents of an audio file.

# Utilities section
https://wiki.archlinux.org/title/List_of_applications/Utilities
## 1. Terminal:
## 2.1 File managers:
## Keyboard layout switchers:
- bxkb — A NETWM compliant keyboard indicator and switcher. It shows a flag of current keyboard in a systray area and allows you to switch to another one.
- gxkb — X11 keyboard layout indicator and switcher.
- qxkb — A keyboard switcher written in Qt.
- xxkb — A lightweight keyboard layout indicator and switcher.
    
**4.3 Keybinding managers**: https://wiki.archlinux.org/title/Keyboard_shortcuts#Xorg

**6.3 System information viewers**:
- agesafetch — A tool for identifying the AGESA version embedded in your AMD system's UEFI firmware.
- alsi — A system information tool for Arch Linux. It can be configured for every other system without even touching the source code of the script.
- archey4 — Python script to display system information alongside the Arch Linux logo.
- dmidecode — It reports information about your system's hardware as described in your system BIOS according to the SMBIOS/DMI standard.
- fastfetch — Like Neofetch, but much faster because written in C.
- hwdetect — Simple script to list modules that are exported in /sys/.
- hwinfo — Powerful hardware detection tool come from openSUSE.
- hw-probe — Tool to probe for hardware, check operability and find drivers with the help of Linux Hardware Database.
- inxi — A script to get system information.
- lshw — A small tool to provide detailed information on the hardware configuration of the machine with CLI and GTK interfaces.
- neofetch — A fast, highly customizable system info script that supports displaying images with w3m.
- nmon — Console based application for monitoring various system components.
- pfetch — A pretty system information tool written in POSIX sh.
- screenfetch — Similar to archey but has an option to take a screenshot. Written in bash.
- GPU-Viewer — GUI to glxinfo, vulkaninfo, clinfo and es2_info; written in Python with GTK.
- hardinfo2 — System Information and Benchmark for Linux Systems.
- KInfoCenter — Centralized and convenient overview of system information for KDE. Part of plasma.
- USBView — Display the topology of devices on the USB bus.

**6.5 Font viewers**:
- Deepin Font Manager — A font management tool for Deepin desktop.
- Font Manager — Simple font management for GTK desktop environments.
- fontpreview — Simple shell script using fzf and sxiv for previewing fonts.
- fontpreview-ueberzug — Shell script inspired by fontpreview that uses ueberzug instead of sxiv.
- Fonty Python — Manage, view and find your fonts.
- GNOME Fonts — Font viewer for GNOME. Part of gnome.
- gtk2fontsel — Font selection and preview tool.
- KFontview — KDE application to view and install different types of fonts. Part of plasma.
- MATE Font Viewer — Font viewer for MATE.


# Others section

## Password managers
- 1Password — Proprietary tool for 1Password password manager.
- Bitwarden — Open source password manager with desktop, mobile, browser, and CLI versions. Cloud or self-hosted.
- gopass — Advanced console based password manager, supporting GnuPG and other backends.
- Himitsu — Secret storage manager.
- KeePassC — Curses-based password manager compatible to KeePass v.1.x.
- LastPass — Hosted password manager.
- pass — Simple console-based password manager featuring flat text file organization and GnuPG encryption.
- passage — A fork of password-store that uses age as backend.
- pwsafe — Unix command-line program that manages encrypted password databases.
- tpm — Tiny password manager, inspired by pass, written entirely in POSIX shell.
- Vault — Proprietary tool for managing secrets.
- Authenticator — Open source, two-factor authentication application built for GNOME.
 Figaro's Password Manager 2 — GTK2 port of Figaro's Password Manager with some new enhancements.
- KDE Wallet Manager — Tool to manage the passwords on your system. By using the KDE wallet subsystem, it not only allows you to keep your own secrets but also to access and manage the passwords of every application that integrates with the wallet. Part of kde-utilities.
- KeePass Password Safe — Mono-based password manager, which helps you to manage your passwords in a secure way.
- KeePassXC — Community fork of KeePassX with more active development. Compatible with KeePass v.1.x (import only) and KeePass v.2.x.
- Key Rack — Password manager for GNOME to view and edit keys, like passwords or tokens, stored by apps.
- Keysmith — OTP generation software by KDE. Part of kde-utilities.
- OTPClient — Highly secure and easy to use GTK software for two-factor authentication that supports both Time-based One-time Passwords (TOTP) and HMAC-Based One-Time Passwords (HOTP).
- Passbook — Modern password manager for GNOME.
- Password Safe — Simple and secure password manager.
- Proton Pass — European-hosted password manager.
- QtPass — GUI for pass, the standard unix password manager.
- Revelation — Password manager for the GNOME desktop.
- Seahorse — GNOME application for managing encryption keys and passwords in the GNOME Keyring. Part of gnome-extra.
- Secrets — Password manager for GNOME which makes use of the KeePass v.4 format.

**Time management**:
- Calcurse — Text-based ncurses calendar and scheduling system (supports CalDAV)
- khal — Command-line (non-interactive) and ncurses (interactive) calendar system (supports CalDAV)
- gcalcli — Command-line (non-interactive) Google Calendar for event management and agendas.
- mail2rem — Small script for importing .ics calendars from Maildir to Remind calendar.
- Pal — Very lightweight calendar with both interactive and non-interactive interfaces.
- pcal — A tool to create pdf calendars from pcal input which can be exported by some calendar programs.
- Remind — Highly sophisticated text-based calendaring and notification system.
- When — Simple personal calendar program.
- Wyrd — Text-based front-end to Remind, a calendar and alarm program used on UNIX and Linux computers.
- Agenda — Calendar application built with MauiKit. Part of maui.
- Calindori — Calendar application for Plasma Mobile.
- CoreTime — Very simple Clock/Calendar application which shows a clock, supports alarms, reminders, a stop watch and a timer. Part of C-Suite.
- Deepin Calendar — Calendar application for Deepin.
- etmtk (Event and Task Manager) — Simple application with a "Getting Things Done!" approach to handling events, tasks, activities, reminders and projects.
- GNOME Calendar — Calendar application for GNOME. Part of gnome.
- KAlarm — Personal alarm message, command and email scheduler, part of kde-pim.
- Kongress — Companion application for conferences made by KDE. Part of kde-utilities.
- KOrganizer — Calendar and scheduling program, part of kde-pim.
- Merkuro Calendar — Calendar application using Akonadi that supports both local and online calendars: Nextcloud, Google Calendar, Outlook, Caldav and more. Part of kde-pim.
- Nextcloud Calendar — Calendar app for Nextcloud.
- Outspline — Extensible outliner with advanced time management features, supporting events with complex recurrence schemes.
- TkRemind — Sophisticated calendar and alarm program.

**Task management**:
- c3 — A multi-platform TUI todo manager that extends calcurse's todo format to have a tree-like dependency structure, and even more!
- Cfait — Powerful, simple, elegant, and lightweight CalDAV task manager (TUI & GUI).
- dijo — Scriptable, curses-based, digital habit tracker
- Taskbook — Tasks, boards and notes for the command-line habitat.
- Taskell — A command-line kanban board/task manager.
- Taskwarrior — Command-line To-do list application with support for lua customization and more.
- todoman — Command-line To-do list manager (supports CalDAV)
- Todo.txt — Small command-line To-do manager.
- TuDu — Ncurses-based hierarchical To-do list manager with vim-like keybindings.
- Agenda — Simple, fast, no-nonsense to-do (task) list for elementary OS.
- Effitask — Graphical task manager, based on the Todo.txt format.
- Endeavour — Personal task manager for GNOME. Part of gnome-extra.
- Errands — Todo application for those who prefer simplicity.
- Go For It! — Simple and stylish productivity app, featuring a to-do list, merged with a timer that keeps your focus on the current task. To-do lists are stored in the Todo.txt format.
- GTG — Personal tasks and TODO list items organizer for GNOME inspired by the Getting Things Done (GTD) methodology.
- Nextcloud Tasks — Tasks app for Nextcloud.
- Planner — Task manager with Todoist support.
- ptask — GTK task manager based on Taskwarrior.
- sleek — todo.txt app with modern GUI. Based on the Electron platform.
- TickTick — Is a simple and effective to-do list and task manager app with seamless cloud synchronization across all your devices
- Zanshin — To-do management application for KDE. Part of kde-pim.
  
**Financial management**:
- Beancount — A double-entry bookkeeping computer language that lets you define financial transaction records in a text file, read them in memory, generate a variety of reports from them, and provides a web interface.
- hledger — An accounting program for tracking money, time, or any other commodity, using double-entry accounting and a simple, editable file format. hledger is inspired by and largely compatible with ledger.
- Ledger — Ledger is a powerful, double-entry accounting system that is accessed from the UNIX command-line.
- Eqonomize! — Cross-platform personal accounting software, with focus on efficiency and ease of use for the small household economy.
- ERPNext — Free and open source Enterprise Resource Planning (ERP).
- GnuCash — Financial application that implements a double-entry book-keeping system with features for small business accounting.
- Grisbi — Personal finance system which manages third party, expenditure and receipt categories, as well as budgetary lines, financial years, and other information that makes it suitable for associations.
- HomeBank — Easy to use finance manager that can analyse your personal finance in detail using powerful filtering tools and graphs.
- KMyMoney — Personal finance manager that operates in a similar way to Microsoft Money. It supports different account types, categorisation of expenses and incomes, reconciliation of bank accounts and import/export to the “QIF” file format.
- Kresus — Self-hosted personal finance management software. It automatically retrieves every day all your new bank transactions and lets you categorize them, study them through charts and establish a budget.
- Manager — Proprietary accounting software for small business.
- Money Manager EX — An easy-to-use personal finance suite
- Odoo — Open source ERP system purely in Python. Previously known as OpenERP.
- Skrooge — Personal finances manager for the KDE desktop.

**6.3 AI applications**
*6.3.1 Desktop clients*:
- AIOne — An all-in-one AI desktop application that provides access to ChatGPT, Gemini, and Claude (uses system-wide Electron).
- Alpaca AI — A flexible client for Ollama, enabling local AI model usage and integration with third-party services like ChatGPT and Gemini.
- BrowserOS — An open-source agentic browser that runs AI agents locally.
- Cherry Studio — Desktop client for multiple LLM providers (OpenAI, Claude, LocalAI, etc.).
- Chatbox — A cross-platform desktop application for interacting with GPT-4 and GPT-3.5 models via the OpenAI API.
- ChatWise — Fast AI chatbot desktop application.
- clara-verse — Privacy-first, client-side AI assistant WebUI for LLMs with ComfyUI integration.
- GPT4All — A lightweight solution for running large language models locally on any device.
- Jan — An easy-to-use platform for deploying and managing AI models directly on your PC.
- Lobe Chat — A modern, extensible chat framework for LLMs, supporting multiple AI providers, multi-modal interactions, and plugins.
- LocalAI — Free, Open Source OpenAI alternative with CPU optimizations.
- NextChat — A cross-platform ChatGPT client.
- noi-desktop — AI-powered desktop assistant for exploration and task automation.
- Open-GPT — A ChatGPT client using the OpenAI API.
- SillyTavern — A feature-rich local interface for interacting with large language models (LLMs), generating images, and synthesizing speech.
- Mycroft — Intelligent personal assistant and knowledge navigator with speech recognition.
*Terminal clients*:
- AIChat NG — An enhanced fork of AIChat with advanced features for terminal-based AI interactions.
- Gemini CLI — Open-source AI agent that brings the power of Google Gemini directly into your terminal.
- GitHub Copilot CLI — Official CLI interface for GitHub Copilot coding assistant.
- TLM — Local CLI Copilot powered by Ollama.
- ShellGPT — A productivity-focused CLI tool powered by OpenAI's ChatGPT, designed for efficient command-line workflows.


---  
# Promt para comparar
Can you make a comparison between ____ for linux to search for the overall best and wich ones i should avoid? 
This is a (non extensive) list of programs:

Now start removing options based on the amount of features they share.


# Other must in hyrpland
- waybar
- eww
- rofi (o wofi, o wmenu)??????

## Others
- git (creo)
- gitlab???
- vs-code(ium)

