#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	JSON
%define	pnam	XS
%include	/usr/lib/rpm/macros.perl
Summary:	JSON::XS - JSON serialising/deserialising, done correctly and fast
Summary(pl.UTF-8):	JSON::JS - serializacja/deserializacja JSON wykonana poprawnie i szybko
Name:		perl-JSON-XS
Version:	3.02
Release:	1
Epoch:		2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d4078f18003b50be970709a77b6afbf
URL:		http://search.cpan.org/dist/JSON-XS/
BuildRequires:	perl-Encode
BuildRequires:	perl-Types-Serialiser
BuildRequires:	perl-common-sense
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

As this is the n-th-something JSON module on CPAN, what was the reason
to write yet another JSON module? While it seems there are many JSON
modules, none of them correctly handle all corner cases, and in most
cases their maintainers are unresponsive, gone missing, or not
listening to bug reports for other reasons.

%description -l pl.UTF-8
Ten moduł konwertuje struktury danych Perla do formatu JSON i
odwrotnie. Jego podstawowym celem jest poprawne działanie, a drugim -
szybkość. W celu osiągnięcia tego drugiego celu został napisany w C.

Jako że jest to już któryś moduł JSON w CPAN-ie, musiała istnieć jakaś
przyczyna dla napisania kolejnego modułu JSON. O ile istnieje wiele
takich modułów, żaden z nich nie obsługiwał wszystkich skrajnych
przypadków i w większości przypadków utrzymujący moduły nie
odpowiadali, zaginęli lub z innych powodów nie zwracali uwagi na
zgłoszenia błędów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/json_xs
%{perl_vendorarch}/JSON/XS.pm
%{perl_vendorarch}/JSON/XS
%dir %{perl_vendorarch}/auto/JSON
%dir %{perl_vendorarch}/auto/JSON/XS
%attr(755,root,root) %{perl_vendorarch}/auto/JSON/XS/*.so
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
