Summary:	libmorph Morphing Library
Summary(pl.UTF-8):   libmorph biblioteka do morfingu
Name:		libmorph
Version:	0.1.2
Release:	6
License:	GPL
Group:		Libraries
Source0:	http://wine.sexcity.pl/morpheus/%{name}-%{version}.tar.gz
# Source0-md5:	d7df93c012418ec16ed6773bb5cb926f
Patch0:		%{name}-amfix.patch
URL:		http://wine.sexcity.pl/morpheus/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that provides loaders for various popular formats of meshes
(3D modeler object files). The meshes are stored in memory in
structures and arrays easily accessible via 3D rendering API's like
OpenGL[TM].

Currently it supports LWO (LightWave) and 3DS (3D Studio) formats.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcje wczytujące różne popularne formaty
siatek (plików obiektów z modelerów 3D). Siatki są zapisywane w
pamięci w strukturach i tablicach łatwo dostępnych poprzez API
renderujące typu OpenGL[TM].

W chwili obecnej obsługuje formaty LWO (LightWave) i 3DS (3D Studio).

%package devel
Summary:	LibMorph development files
Summary(pl.UTF-8):   Pliki programistyczne LibMorph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LibMorph library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilacji programów używających
libmorph.

%package static
Summary:	LibMorph static library
Summary(pl.UTF-8):   Statyczna biblioteka LibMorph
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libmorph library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libmorph.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/morph/loaders/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libmorph*.so.*.*.*
%dir %{_libdir}/morph
%dir %{_libdir}/morph/loaders
%attr(755,root,root) %{_libdir}/morph/loaders/*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/morph

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
