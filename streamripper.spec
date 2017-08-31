Summary:	Shoutcast and icecast compatible streams recorder
Name:		streamripper
Version:	1.64.6
Release:	8%{?dist}
URL:		http://streamripper.sourceforge.net/
License:	GPLv2
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

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
%setup -q
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
