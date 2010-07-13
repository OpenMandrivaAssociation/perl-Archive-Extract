%define	upstream_name	 Archive-Extract
%define upstream_version 0.42

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A generic archive extracting mechanism
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Archive/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(IPC::Cmd)                  >= 0.360.0
BuildRequires:  perl(Module::Load::Conditional) >= 0.40.0
BuildRequires:  perl-version
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz, .gz, .Z,
tar.bz2, .tbz, .bz2 or .zip without having to worry how it does so, or use
different interfaces for each type by using either perl modules, or commandline
tools on your system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Archive/*
%{_mandir}/*/*
