#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	JSON
%define	pnam	XS
Summary:	JSON::XS - JSON serialising/deserialising, done correctly and fast
#Summary(pl.UTF-8):	
Name:		perl-JSON-XS
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/JSON-XS-1.11.tar.gz
# Source0-md5:	b3cb4892921016863a2c50d64a42c874
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/JSON-XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be
fast. To reach the latter goal it was written in C.

As this is the n-th-something JSON module on CPAN, what was the reason
to write yet another JSON module? While it seems there are many JSON
modules, none of them correctly handle all corner cases, and in most cases
their maintainers are unresponsive, gone missing, or not listening to bug
reports for other reasons.

See COMPARISON, below, for a comparison to some other JSON modules.

See MAPPING, below, on how JSON::XS maps perl values to JSON values and
vice versa.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/JSON/*.pm
%dir %{perl_vendorarch}/auto/JSON/XS
%{perl_vendorarch}/auto/JSON/XS/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/JSON/XS/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
