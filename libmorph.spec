Summary:	libmorph Morphing Library
Summary(pl):	libmorph biblioteka do morfingu
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

%description -l pl
Ta biblioteka udostêpnia funkcje wczytuj±ce ró¿ne popularne formaty
siatek (plików obiektów z modelerów 3D). Siatki s± zapisywane w
pamiêci w strukturach i tablicach ³atwo dostêpnych poprzez API
renderuj±ce typu OpenGL[TM].

W chwili obecnej obs³uguje formaty LWO (LightWave) i 3DS (3D Studio).

%package devel
Summary:	LibMorph development files
Summary(pl):	Pliki programistyczne LibMorph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LibMorph library.

%description devel -l pl
Pliki nag³ówkowe potrzebne do kompilacji programów u¿ywaj±cych
libmorph.

%package static
Summary:	LibMorph static library
Summary(pl):	Statyczna biblioteka LibMorph
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libmorph library.

%description static -l pl
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
