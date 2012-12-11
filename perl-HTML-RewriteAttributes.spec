%define upstream_name    HTML-RewriteAttributes
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Concise attribute rewriting
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/HTML-RewriteAttributes/
Source0:	http://www.cpan.org/authors/id/S/SA/SARTAK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::Tagset)
BuildRequires:	perl(URI)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
# rpm doesn't catch this
Requires:	perl(HTML::Parser)

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
chmod -R u+w %{buildroot}/*

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Nov 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 599559
- update to new version 0.04

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 403258
- rebuild using %%perl_convert_version

* Thu Dec 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdv2009.1
+ Revision: 309994
- import perl-HTML-RewriteAttributes


* Thu Dec 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdv2009.0
- initial Mandriva package (fedora import)

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Specfile autogenerated by cpanspec 1.77.
