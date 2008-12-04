Summary:        Concise attribute rewriting
Name:           perl-HTML-RewriteAttributes
Version:        0.03
Release:        %mkrel 1
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-RewriteAttributes/
Source0:        http://www.cpan.org/authors/id/S/SA/SARTAK/HTML-RewriteAttributes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
BuildRequires:  perl(Test::More)
# rpm doesn't catch this
Requires:       perl(HTML::Parser)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

%prep

%setup -q -n HTML-RewriteAttributes-%{version}

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

