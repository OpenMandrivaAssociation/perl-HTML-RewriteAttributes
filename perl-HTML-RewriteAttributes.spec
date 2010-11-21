%define upstream_name    HTML-RewriteAttributes
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Concise attribute rewriting
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/HTML-RewriteAttributes/
Source0:    http://www.cpan.org/authors/id/S/SA/SARTAK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
BuildRequires:  perl(Test::More)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
# rpm doesn't catch this
Requires:       perl(HTML::Parser)

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
