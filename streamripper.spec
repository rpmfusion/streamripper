Summary:	Shoutcast and icecast compatible streams recorder
Name:		streamripper
Version:	1.64.6
Release:	2%{?dist}
Group:		Applications/Multimedia
URL:		http://streamripper.sourceforge.net/
License:	GPLv2
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libogg-devel
<<<<<<< streamripper.spec
BuildRequires:	libvorbis-devel
BuildRequires:	libmad-devel
BuildRequires:	tre-devel
BuildRequires:	faad2-devel
BuildRequires:	glib2-devel >= 2.16
=======
BuildRequires:  libvorbis-devel
BuildRequires:  libmad-devel
BuildRequires:  tre-devel
BuildRequires:  faad2-devel
BuildRequires:  glib2-devel >= 2.6
>>>>>>> 1.4


%description

Streamripper records shoutcast and icecast compatible streams, in their
native format. The following formats are supported: mp3, nsv, aac, and
ogg. The meta data within the stream are interpreted to determine the
beginning and end of each song, and stores the songs on your hard  disk
as individual files. In addition, streamripper includes a relay server
for listening to the station while you are recording.

%prep
%setup -q
<<<<<<< streamripper.spec

=======
>>>>>>> 1.4
chmod 0644 ./lib/charset.h

%build
## To be sure we will not use the embedded libmad
rm -rf ./libmad-*

%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p -c"

<<<<<<< streamripper.spec

=======
>>>>>>> 1.4

%files
%defattr(-,root,root,-)
%doc README THANKS *.txt CHANGES COPYING 
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf %{buildroot}

%changelog
* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

<<<<<<< streamripper.spec
* Thu Apr 30 2009 kwizart < kwizart at gmail.com > - 1.64.6-1
- Update to 1.64.6

=======
* Thu Apr 30 2009 Nicolas Chauvet <kwizart@gmail.com> - 1.64.6-1
- Update release.

>>>>>>> 1.4
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
