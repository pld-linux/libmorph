Summary:	libmorph Morphing Library
Summary(pl):	libmorph biblioteka do morfingu
Name:		libmorph
Version:	0.1.2
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	http://wine.sexcity.pl/morpheus/%{name}-%{version}.tar.gz
URL:		http://wine.sexcity.pl/morpheus/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A library that provides loaders for various popular formats of meshes
(3d modeler object files). The meshes are stored in memory in
structures and arrays easily accessible via 3D rendering API's like
OpenGL[TM].

%description -l pl
LibMorph wspomaga wy�wietlanie projekt�w 3D, w chwili obecnej
wspomaga:
 - LWO - LightWave
 - 3DS - 3D Studio

%package devel
Summary:	LibMorph development
Summary(pl):	LibMorph development
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files, and debug information.

%description -l pl devel
Pliki nag��wkowe potrzebne do kompilacji program�w u�ywaj�cych
libmorph.

%package static
Summary:	LibMorph static
Summary(pl):	LibMorph static
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static library of libmorph.

%description -l pl static
Biblioteka libmorph linkowna statycznie.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
rm -f missing
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmorph*.so.*.*.*
%dir %{_libdir}/morph
%dir %{_libdir}/morph/loaders
%attr(755,root,root) %{_libdir}/morph/loaders/*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(644,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/morph/loaders/*.la
%{_includedir}/morph

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/morph/loaders/*.a
