%define	modname	Archive-Extract
%define	modver	0.60

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	2

Summary:	A generic archive extracting mechanism
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Archive/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Cmd)			>= 0.360.0
BuildRequires:	perl(Module::Load::Conditional)	>= 0.40.0
BuildRequires:	perl-version
BuildRequires:	perl-JSON-PP
BuildArch:	noarch

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz, .gz, .Z,
tar.bz2, .tbz, .bz2 or .zip without having to worry how it does so, or use
different interfaces for each type by using either perl modules, or commandline
tools on your system.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/Archive/*
%{_mandir}/*/*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.600.0-1
- cleanups
- new version

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.520.0-4mdv2012.0
+ Revision: 765053
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.520.0-3
+ Revision: 763477
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.520.0-2
+ Revision: 763042
- rebuild

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1
+ Revision: 662007
- update to new version 0.52

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.0-1
+ Revision: 659885
- update to new version 0.50

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 630618
- update to new version 0.48

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.460.0-1mdv2011.0
+ Revision: 595072
- update to new version 0.46

* Wed Oct 13 2010 Buchan Milne <bgmilne@mandriva.org> 0.440.0-1mdv2011.0
+ Revision: 585506
- New version 0.44

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2011.0
+ Revision: 552254
- update to 0.42

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 487047
- update to 0.38

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.1
+ Revision: 470463
- update to 0.36

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2010.0
+ Revision: 408913
- rebuild using %%perl_convert_version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2010.0
+ Revision: 390323
- update to new version 0.34

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2010.0
+ Revision: 386988
- update to new version 0.32

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2009.1
+ Revision: 315097
- update to new version 0.30

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2009.1
+ Revision: 292020
- update to new version 0.28

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.26-2mdv2009.0
+ Revision: 289341
- restore the spec file

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2008.1
+ Revision: 159907
- update to new version 0.26

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2008.1
+ Revision: 98020
- update to new version 0.24
- update to new version 0.24

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.22-1mdv2008.0
+ Revision: 42850
- Import perl-Archive-Extract




* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.22-1mdv2007.1
- initial package
