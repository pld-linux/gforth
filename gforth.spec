Summary:     GNU Forth Language
Summary(pl): Kompilator GNU Forth 
Name:        gforth
Version:     0.4.0
Release:     1
Copyright:   GPL
Group:       Languages
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz 
Patch0:      gforth-makefile.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history and a powerful locals
facility, and it even has (the beginnings of) a manual. Gforth employs
traditional implementation techniques: its inner innerpreter is
indirect or direct threaded.  Gforth is distributed under the GNU
General Public license (see COPYING).

%description -l pl
Gforth jest szybk± i przenoszaln± implementacj± jêzyka ANS Forth.
Dobrae wspólpracuje z edytorem Emacs oferuj±c takie cechy jak kompletowanie
i historiê wprowadzania ci±gów znaków.

%prep
%setup -q
%patch0 -p1

%build
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/gforth.info*

%post
/sbin/install-info %{_infodir}/gforth.info.gz /usr/info/dir \
--section "Programming:" --entry \
"* Gforth: (gforth.info).                       The GNU ANS Forth."

%preun
/sbin/install-info --delete %{_infodir}/gforth.info.gz /usr/info/dir \
--section "Programming:" --entry \
"* Gforth: (gforth.info).                       The GNU ANS Forth."


%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644,root,root,755)
%doc README TAGS BUGS ToDo
%attr(755,root,root) %{_bindir}/*
%{_libdir}/gforth
%{_infodir}/*info*
%{_mandir}/man1/*
%{_datadir}/gforth
