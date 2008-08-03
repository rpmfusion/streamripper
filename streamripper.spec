Summary:	Shoutcast and icecast compatible streams recorder
Name:		streamripper
Version:	1.62.3
Release:	8%{?dist}
Group:		Applications/Multimedia
URL:		http://streamripper.sourceforge.net/
License:	GPLv2
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libmad-devel
BuildRequires:  tre-devel
BuildRequires:  faad2-devel

Patch0: streamripper-vswprintf-no-redef.patch

%description

Streamripper records shoutcast and icecast compatible streams, in their
native format. The following formats are supported: mp3, nsv, aac, and
ogg. The meta data within the stream are interpreted to determine the
beginning and end of each song, and stores the songs on your hard  disk
as individual files. In addition, streamripper includes a relay server
for listening to the station while you are recording.

%prep
%setup -q
%patch0 -p1
chmod 0644 ./lib/charset.h

%build
## To be sure we will not use the embedded libmad
rm -rf ./libmad-*
## To be sure we will not use the embedded tre
rm -rf ./tre-*

%configure --disable-static
make %{?_smp_mflags} CFLAGS="%{optflags} -L%{_libdir}"


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p -c"

## man page must be converted to utf8
%define man_ori %{buildroot}/%{_mandir}/man1/streamripper.1
%define man_tmp %{man_ori}.utf8
iconv -f ISO-8859-1 -t utf8 %{man_ori} -o %{man_tmp}
mv -f %{man_tmp} %{man_ori}

%files
%defattr(-,root,root,-)
%doc README THANKS *.txt CHANGES COPYING 
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf %{buildroot}

%changelog
* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.62.3-8
- rebuild

* Sat Nov 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.62.3-7
- rebuilt


* Mon Sep 03 2007 Patrice Bouchand <patrice.bouchand.fedora@gmail.com> 1.62.3-6
- New streamripper release

* Sat Sep 01 2007 Patrice Bouchand <patrice.bouchand.fedora@gmail.com> 1.62.2-5
- Force Makefile to search lib in _libdir
- Add INSTALL="install -p -c" for make install

* Mon Aug 13 2007 Patrice Bouchand <patrice.bouchand.fedora@gmail.com> 1.62.2-4
- New release of streamripper
- Spec clean-up

* Thu Aug 9 2007 Patrice Bouchand <patrice.bouchand.fedora@gmail.com> 1.62.1-3
- Force to use external tre lib.

* Wed Aug 8 2007 Patrice Bouchand <patrice.bouchand.fedora@gmail.com> 1.62.1-2
- Convert man page to UTF8
- Add streamripper-vswprintf-no-redef.patch

* Wed Aug 8 2007 Patrice Bouchand <patrice.bouchand.fedora@gmail.com> 1.62.1-1
- Initial Fedora release
