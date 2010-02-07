Summary:	A sandbox game, based on physics
Name:		caph
Version:	091231
Release:	0.3
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/project/caphgame/caph/caph-091231/%{name}-src-%{version}.tar.bz2
# Source0-md5:	26d743ed2b82726dea8cd3c4780b3adb
Source1:	http://dl.sourceforge.net/project/caphgame/caph/caph-091231/%{name}-data-%{version}.tar.bz2
# Source1-md5:	42877f73bba16d835391ddaf747ccdd3
Patch0:		%{name}-libpng.patch
Patch1:		%{name}-sysdatadir.patch
Patch2:		%{name}-mapsdir.patch
URL:		http://caphgame.sourceforge.net/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	SDL-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a sandbox game, based on physics. The game target is to make
contact red object with green object. You can use various objects,
solid, wire (rope), and bendable objects. Gravitation will help you.

%prep
%setup -q -n %{name}-src
tar xvf %{SOURCE1}

%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i "1 s,/sh,/bash," src/{build,mkgen}
%{__sed} -i "s,libgl,gl," src/build

%build
cd src
CFLAGS="%{rpmcflags}" \
LFLAGS="%{rpmldflags}" \
./build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install bin/caph $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r caph-data/share/caph/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/caph/CHANGELOG doc/caph/README
%attr(755,root,root) %{_bindir}/caph
%{_datadir}/%{name}
