%define		_realname	linky
Summary:	Easy access to open links and pictures on webpages
Summary(pl.UTF-8):	Łatwy dostęp do otwierania odnośników i obrazów na stronach WWW
Name:		mozilla-addon-%{_realname}
Version:	2.1.0
%define	_foover	%(echo %{version} | tr -d .)
Release:	3
License:	?
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/linky/%{_realname}-%{_foover}.xpi
# Source0-md5:	45b2325c2faa94de4fbc7ed66e3a5dc7
Source1:	%{_realname}-installed-chrome.txt
URL:		http://%{_realname}.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Linky is a very simple addon to the context menu that provide you with
the following:

* Opens all links in a selection in new tabs or windows
* Finds and opens link in plain text in a new tab or window
* Opens all links on page in new tabs or windows
* Open all links that appears to be linking to an image in new tabs
  or windows
* Shows all links that appears to be linking to an image in one new
  tab or window
* Open all links that appears to be linking to an image in one new tab
  or window
* Download all links on page
* Validate all links on page
* Select links Dialog
* Preferences panel

%description -l pl.UTF-8
Linky to bardzo prosty dodatek do menu kontekstowego dostarczający
następującą funkcjonalność:

- otwieranie wszystkich wybranych odnośników w nowych panelach lub
  okienkach
- znajdowanie i otwieranie odnośników z dokumentów czysto tekstowych
  w nowym panelu lub okienku
- otwieranie wszystkich odnośników ze strony w nowych panelach lub
  okienkach
- otwieranie wszystkich odnośników wyglądające na odnośniki do
  obrazków w nowych panelach lub okienkach
- pokazywanie wszystkich odnośników wyglądających na odnośniki do
  obrazków w jednym nowym panelu lub okienku
- otwieranie wszystkich odnośników wyglądających na odnośniki do
  obrazków w jednym nowym panelu lub okienku
- ściąganie wszystkich odnośników ze strony
- sprawdzanie wszystkich odnośników ze strony
- okno dialogowe wyboru odnośników
- panel ustawień

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/*-installed-chrome.txt
