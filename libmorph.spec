Summary:	libmorph
Summary(pl):	libmorph
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

%package devel
Summary:	LibMorph development
Summary(pl):	LibMorph development
Group:		X11/Libraries/Development
Grop(pl):	X11/Biblioteki/Programowanie

%description devel
%description -l pl devel

%package static
Summary:	LibMorph static
Summary(pl):	LibMorph static
Group:		X11/Libraries/Development
Grop(pl):	X11/Biblioteki/Programowanie

%description static
%description -l pl static


%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)

%files devel
%defattr(644,root,root,755)
%doc
%attr(,,)

%files static
%defattr(644,root,root,755)
%doc
%attr(,,)
