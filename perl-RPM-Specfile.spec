#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	RPM
%define		pnam	Specfile
Summary:	RPM::Specfile - Perl extension for creating RPM specfiles
Summary(pl.UTF-8):	RPM::Specfile - rozszerzenie Perla do tworzenia plików .spec dla RPM-a
Name:		perl-RPM-Specfile
Version:	1.51
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	023b47c72581ac2190487b7ad0185bcf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple module for creation of RPM Spec files. Used by cpanflute2 to
turn CPAN tarballs into RPM modules. See the included script
cpanflute2 for usage; documentation coming soon.

%description -l pl.UTF-8
Prosty moduł do tworzenia plików .spec dla RPM-a. Jest używany przez
cpanflute2 do zamiany paczek CPAN na moduły RPM. Sposób użycia można
znaleźć w załączonym skrypcie cpanflute2 - dokumentacja wkrótce.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/cpanflute2 $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
