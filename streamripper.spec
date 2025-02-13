# https://bugzilla.rpmfusion.org/show_bug.cgi?id=5849
%global _lto_cflags %{nil}

Summary:	Shoutcast and icecast compatible streams recorder
Name:		streamripper
Version:	1.64.6
Release:	24%{?dist}
URL:		http://streamripper.sourceforge.net/
License:	GPLv2
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz 
Patch0:     buildfix.patch

BuildRequires:	gcc
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libmad-devel
BuildRequires:	tre-devel
BuildRequires:	faad2-devel
BuildRequires:	glib2-devel >= 2.16


%description

Streamripper records shoutcast and icecast compatible streams, in their
native format. The following formats are supported: mp3, nsv, aac, and
ogg. The meta data within the stream are interpreted to determine the
beginning and end of each song, and stores the songs on your hard  disk
as individual files. In addition, streamripper includes a relay server
for listening to the station while you are recording.

%prep
%autosetup -p1
chmod 0644 ./lib/charset.h

%build
## To be sure we will not use the embedded libmad
rm -rf ./libmad-*

%configure --disable-static
%make_build


%install
rm -rf %{buildroot}
%make_install


%files
%doc README THANKS *.txt CHANGES
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.64.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.64.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.64.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.64.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.64.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.64.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Leigh Scott <leigh123linux@gmail.com> - 1.64.6-16
- Disable LTO (rfbz #5849)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.64.6-11
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.64.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.64.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.64.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.64.6-7
- Update spec file

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.64.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.64.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.64.6-4
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.64.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.63.5-3
- rebuild for new F11 features

* Fri Aug 08 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.63.5-2
- rebuild for RPM Fusion

* Fri Aug 08 2008 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.63.5-1
- New streamripper release

* Sat Nov 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.62.3-7
- rebuilt

* Mon Sep 03 2007 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.62.3-6
- New streamripper release

* Sat Sep 01 2007 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.62.2-5
- Force Makefile to search lib in _libdir
- Add INSTALL="install -p -c" for make install

* Mon Aug 13 2007 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.62.2-4
- New release of streamripper
- Spec clean-up

* Thu Aug 9 2007 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.62.1-3
- Force to use external tre lib.

* Wed Aug 8 2007 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.62.1-2
- Convert man page to UTF8
- Add streamripper-vswprintf-no-redef.patch

* Wed Aug 8 2007 Patrice Bouchand <patrice[DOT]bouchand[DOT]fedora[AT]gmail[DOT]com> 1.62.1-1
- Initial Fedora release
