#
# Conditional build:
%bcond_without	nas		# don't build NAS support
%bcond_without	gtkspell	# don't build automatic spellchecking
#
%define		_modver	1.02
Summary:	ScatterChat
Summary(pl):	ScatterChat
Name:		scatterchat
Version:	1.0.1
Release:	0.5
License:	GPLv2
Group:		X11/Applications
Source0:	http://www.rit.edu/~jst2912/%{name}-%{version}.tar.bz2
# Source0-md5:	1e1eabf92f191c97aaf9bf75d97154f3
Source1:	http://www.rit.edu/~jst2912/%{name}-module-%{_modver}.tar.bz2
# Source1-md5:	a1ed47e51448527c52496fb7bc551c89
URL:		http://www.scatterchat.com
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
%{?with_gtkspell:BuildRequires: gtkspell-devel}
BuildRequires:	libgcrypt-devel
%{?with_nas:BuildRequires: nas-devel}
Requires:	scatterchat-modules
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

%description -l pl
ScatterChat to BROÑ HAKTYWISTY zaprojektowana, aby pozwoliæ
nietechnicznym aktywistom praw cz³owieka i dysydentom politycznym
komunikowaæ siê bezpiecznie i anonimowo w czasie dzia³ania na
wrogim terenie. Jest przydatna tak¿e w uk³adach korporacyjnych lub
innych sytuacjach, kiedy po¿±dana jest prywatno¶æ.

Jest to bezpieczny klient systemu komunikacji (oparty na programie
Gaim) udostêpniaj±cy szyfrowanie miêdzy koñcami, zintegrowany routing
"na cebulkê" przy u¿yciu Tora, bezpieczne przesy³anie plików i ³atw±
do przeczytania instrukcjê.

Cechy zwi±zane z bezpieczeñstwem obejmuj± odporno¶æ na czê¶ciowe
z³amanie poprzez ca³kowit± dyskrecjê przekazywania, odporno¶æ na
ataki powtórzeniowe i ograniczon± odporno¶æ na analizê ruchu...
wszystko to wymuszone dziêki bezpiecznemu sposobowi zaprojektowania.

%package modules
Summary:	Standalone scatterchat module
Summary(pl):	Wolnostoj±cy modu³ scatterchat
Group:		X11/Applications

%description modules
Stanalone scatterchat module.

%description modules -l pl
Wolnostoj±cy modu³ scatterchat.

%package devel
Summary:	Header files for scatterchat
Summary(pl):	Pliki nag³ówkowe scatterchata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for scatterchat.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe scatterchata.

%prep
%setup -q -a1
%patch0 -p0

%build
%configure \
	%{?with_nas:--enable-nas} \
	%{!?with_gtkspell:--disable-gtkspell}
%{__make}

cd %{name}-module-%{_modver}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-executable
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%{__make} install \
	-C %{name}-module-%{_modver} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/blackchat-gaim/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS PROGRAMMING_NOTES README
%attr(755,root,root) %{_bindir}/scatterchat
%attr(755,root,root) %{_libdir}/libgaim-remote.so.*.*.*
%dir %{_libdir}/blackchat-gaim
%attr(755,root,root) %{_libdir}/blackchat-gaim/*.so
%{perl_vendorarch}/Gaim.pm
%dir %{perl_vendorarch}/auto/Gaim
%{perl_vendorarch}/auto/Gaim/*
%{_desktopdir}/scatterchat.desktop
%{_mandir}/man1/*.1*
%{_mandir}/man3/Gaim.3pm*
%{_pixmapsdir}/blackchat-gaim
%{_pixmapsdir}/gaim.png
%{_datadir}/sounds/blackchat-gaim

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scatterchatmod

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgaim-remote.so
%{_libdir}/libgaim-remote.la
%{_includedir}/blackchat-gaim
%{_pkgconfigdir}/gaim.pc
