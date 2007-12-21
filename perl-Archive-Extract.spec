%define	module	Archive-Extract
%define name	perl-%{module}
%define	modprefix Archive

%define version 0.24

%define	rel	1
%define release %mkrel %{rel}

Summary:	A generic archive extracting mechanism
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root
BuildRequires:	perl(IPC::Cmd) >= 0.36 perl(Module::Load::Conditional) >= 0.04 perl-version


%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz, .gz, .Z,
tar.bz2, .tbz, .bz2 or .zip without having to worry how it does so, or use
different interfaces for each type by using either perl modules, or commandline
tools on your system.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/%{modprefix}/*
%{_mandir}/*/*

%clean
rm -rf %{buildroot}
