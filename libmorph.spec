Summary:	libmorph Morphing Library
Summary(pl):	libmorph biblioteka do morfingu
Name:		libmorph
Version:	0.1.2
Release:	1
Copyright:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	http://wine.sexcity.pl/morpheus/%name-%version.tar.gz
#Patch0:		
#BuildRequires:	
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description

%description -l pl
LibMorph wspomaga wy¶wietlanie projektów 3D, w chwili obecnej
wspomaga :
LWO - LightWave
3DS - 3D Studio 


%package devel
Summary:	LibMorph development
Summary(pl):	LibMorph development
Group:		X11/Libraries/Development
Group(pl):	X11/Biblioteki/Programowanie

%description devel
Header files, and debug information.

%description -l pl devel
Pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych libmorph.

%package static
Summary:	LibMorph static
Summary(pl):	LibMorph static
Group:		X11/Libraries/Development
Group(pl):	X11/Biblioteki/Programowanie

%description static
Static library of libmorph.

%description -l pl static
Biblioteka libmorph linkowna statycznie.

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf AUTHORS ChangeLog NEWS README TODO

strip $RPM_BUILD_ROOT%{_libdir}/*.so.*.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(644,root,root) %{_libdir}/libmorph*.so.*.*.*
%attr(755,root,root) %{_libdir}/morph/loaders/*.so

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/morph/*.h
%attr(644,root,root) %{_libdir}/*.la
%attr(644,root,root) %{_libdir}/libmorphConf.sh
%attr(755,root,root) %{_libdir}/morph/loaders/*.la

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
%attr(755,root,root) %{_libdir}/morph/loaders/*.a
