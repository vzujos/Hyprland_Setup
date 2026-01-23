Las apps con número están ordenadas por preferencia.

Las apps con guiones no están ordenadas y falta indagar o escoger.

Esta lista ya se encuentra revisada hasta la Metadata.

Esta es la fuente:
https://wiki.archlinux.org/title/List_of_applications
(falta revisar: science, documents, internet,other)

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

## Password managers
e

    1Password — Proprietary tool for 1Password password manager.

    https://1password.com/downloads/command-line/ || 1passwordAUR

    Bitwarden — Open source password manager with desktop, mobile, browser, and CLI versions. Cloud or self-hosted.

    https://bitwarden.com/ || bitwarden-cli

    gopass — Advanced console based password manager, supporting GnuPG and other backends.

    https://github.com/justwatchcom/gopass || gopass

    Himitsu — Secret storage manager.

    https://himitsustore.org/ || himitsuAUR

    KeePassC — Curses-based password manager compatible to KeePass v.1.x.

    https://outerhaven.de/keepassc/ || keepasscAUR

    LastPass — Hosted password manager.

    https://www.lastpass.com/ || lastpass-cliAUR

    pass — Simple console-based password manager featuring flat text file organization and GnuPG encryption.

    https://www.passwordstore.org/ || pass

    passage — A fork of password-store that uses age as backend.

    https://github.com/FiloSottile/passage/ || passage-gitAUR

    pwsafe — Unix command-line program that manages encrypted password databases.

    https://github.com/nsd20463/pwsafe || pwsafeAUR

    tpm — Tiny password manager, inspired by pass, written entirely in POSIX shell.

    https://github.com/nmeum/tpm || tpmAUR

    Vault — Proprietary tool for managing secrets.

    https://vaultproject.io/ || vault

Graphical

    1Password — Proprietary graphical user interface for 1Password password manager.

    https://support.1password.com/install-linux/#arch-linux || 1passwordAUR

    Authenticator — Open source, two-factor authentication application built for GNOME.

    https://apps.gnome.org/Authenticator/ || authenticator

    Bitwarden — Open source password manager with desktop, mobile, browser, and CLI versions. Cloud or self-hosted.

    https://bitwarden.com/ || bitwarden

    Figaro's Password Manager 2 — GTK2 port of Figaro's Password Manager with some new enhancements.

    https://als.regnet.cz/fpm2/ || fpm2AUR

    KDE Wallet Manager — Tool to manage the passwords on your system. By using the KDE wallet subsystem, it not only allows you to keep your own secrets but also to access and manage the passwords of every application that integrates with the wallet. Part of kde-utilities.

    https://userbase.kde.org/KDE_Wallet_Manager || kwalletmanager

    KeePass Password Safe — Mono-based password manager, which helps you to manage your passwords in a secure way.

    https://keepass.info/ || keepass

    KeePassXC — Community fork of KeePassX with more active development. Compatible with KeePass v.1.x (import only) and KeePass v.2.x.

    https://keepassxc.org/ || keepassxc

    Key Rack — Password manager for GNOME to view and edit keys, like passwords or tokens, stored by apps.

    https://gitlab.gnome.org/World/key-rack || key-rack

    Keysmith — OTP generation software by KDE. Part of kde-utilities.

    https://apps.kde.org/keysmith/ || keysmith

    OTPClient — Highly secure and easy to use GTK software for two-factor authentication that supports both Time-based One-time Passwords (TOTP) and HMAC-Based One-Time Passwords (HOTP).

    https://github.com/paolostivanin/OTPClient || otpclientAUR

    Passbook — Modern password manager for GNOME.

    https://wiki.gnome.org/Apps/Passbook || passbookAUR

    Password Safe — Simple and secure password manager.

    https://pwsafe.org/ || passwordsafeAUR

    Proton Pass — European-hosted password manager.

    https://proton.me/pass || proton-passAUR

    QtPass — GUI for pass, the standard unix password manager.

    https://qtpass.org/ || qtpass

    Revelation — Password manager for the GNOME desktop.

    https://revelation.olasagasti.info/ || revelationAUR

    Seahorse — GNOME application for managing encryption keys and passwords in the GNOME Keyring. Part of gnome-extra.

    https://wiki.gnome.org/Apps/Seahorse || seahorse

    Secrets — Password manager for GNOME which makes use of the KeePass v.4 format.

    https://apps.gnome.org/Secrets/ || secrets

## File managers

1. Dolphin
    - Con la opción de jpeg creo
2. Thunar
3. Nemo


## Promt para comparar
Can you make a comparison between ____ for linux to search for the overall best and wich ones i should avoid? 
This is a (non extensive) list of programs:

Now start removing options based on the amount of features they share.


