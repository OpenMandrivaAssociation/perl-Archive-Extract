%define	module	Archive-Extract
%define	modprefix Archive

Summary:	A generic archive extracting mechanism
Name:		perl-%{module}
Version:	0.32
Release:	%mkrel 1
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch
BuildRequires:	perl(IPC::Cmd) >= 0.36 perl(Module::Load::Conditional) >= 0.04 perl-version
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/%{modprefix}/*
%{_mandir}/*/*
