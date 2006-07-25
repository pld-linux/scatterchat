
%define		_modver	1.02
Summary:	ScatterChat
Summary(pl):	ScatterChat
Name:		scatterchat
Version:	1.0.1
Release:	0.1
License:	GPLv2
Group:		X11/Applications
Source0:	http://www.rit.edu/~jst2912/%{name}-%{version}.tar.bz2
# Source0-md5:	1e1eabf92f191c97aaf9bf75d97154f3
Source1:	http://www.rit.edu/~jst2912/%{name}-module-%{_modver}.tar.bz2
# Source1-md5:	a1ed47e51448527c52496fb7bc551c89
URL:		http://www.scatterchat.com
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
#BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ScatterChat is a HACKTIVIST WEAPON designed to allow non-technical
human rights activists and political dissidents to communicate
securely and anonymously while operating in hostile territory. It is
also useful in corporate settings, or in other situations where
privacy is desired.

It is a secure instant messaging client (based upon the Gaim software)
that provides end-to-end encryption, integrated onion-routing with
Tor, secure file transfers, and easy-to-read documentation.

Its security features include resiliency against partial compromise
through perfect forward secrecy, immunity from replay attacks, and
limited resistance to traffic analysis... all reinforced through a
pro-actively secure design.

#%description -l pl

%package modules
Summary:	Scatterchat modules
#Summary(pl):	-
Group:		Libraries

%description modules
Scatterchat modules.

#%description modules -l pl

%package devel
Summary:	Header files for scatterchat
Summary(pl):	Pliki nag³ówkowe scatterchata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki ....

%prep
%setup -q -a1

%build
%configure
%{__make}

cd %{name}-module-%{_modver}
%{__aclocal}
%{__automake}
%configure \
	--with-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd %{name}-module-%{_modver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post modules	-p /sbin/ldconfig
%postun modules	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS PROGRAMMING_NOTES README
%attr(755,root,root) %{_bindir}/scatterchat
%attr(755,root,root) %{_libdir}/blackchat-gaim/*.so
%attr(755,root,root) %{_libdir}/libgaim-remote.so.0.0.0
%{_libdir}/perl5/5.8.8/i686-pld-linux-thread-multi/perllocal.pod
%{_libdir}/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/Gaim.pm
%{_libdir}/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/auto/Gaim/.packlist
%{_libdir}/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/auto/Gaim/*
%{_pkgconfigdir}/gaim.pc
%{_desktopdir}/scatterchat.desktop
%{_mandir}/man1/*.1*
%{_mandir}/man3/Gaim.3pm*
%{_pixmapsdir}/blackchat-gaim
%{_pixmapsdir}/gaim.png
%{_datadir}/sounds/blackchat-gaim/*.wav

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/blackchat-gaim/*.la
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/blackchat-gaim/*.h

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libscatterchat.so.1.0.2
