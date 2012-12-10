%define name	gjots2
%define version 2.3.12
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A note jotter in tree structure
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://bhepple.freeshell.org/gjots/
Source:		http://bhepple.freeshell.org/gjots/%{name}-%{version}.tgz
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	pygtk2.0-libglade >= 2.2.0
Requires:	python-gtksourceview
Requires:	openssl
Requires:	gnupg
Requires:	m4
BuildRequires:	imagemagick
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils

%description
GJots2 can be used to organize one's jottings into a tree structure,
adding thoughts and miscellaneous things. Afterwards the notes can be
exported into various formats such as HTML, XML, Postscript, PDF, man etc.
It can also make use of OpenSSL, GPG or ccrypt(1) for encrypting PINs
and passwords.

%prep
%setup -q

%install
rm -rf %{buildroot}
python setup.py install --root=%buildroot
%find_lang %name

# fix desktop file
sed -i -e 's/gjots.png/gjots/' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
	--remove-key=Encoding \
	--remove-category=Application \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

# icons
install -d -m 755 %{buildroot}%{_liconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
convert -geometry 48x48 gjots.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 gjots.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 gjots.png %{buildroot}%{_miconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc %{_docdir}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{py_sitedir}/*
%{_prefix}/lib/%{name}
%{_mandir}/man1/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.3.12-1mdv2011.0
+ Revision: 645177
- update to new version 2.3.12

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 2.3.9-2mdv2011.0
+ Revision: 594808
- rebuild for python 2.7

* Sun Nov 29 2009 Jérôme Brenier <incubusss@mandriva.org> 2.3.9-1mdv2010.1
+ Revision: 471008
- new version 2.3.9
- Requires : python-gtksourceview

* Mon May 18 2009 Jérôme Brenier <incubusss@mandriva.org> 2.3.8-1mdv2010.0
+ Revision: 376828
- update to new version 2.3.8
- fix source url for automatic update

* Sun May 17 2009 Jérôme Brenier <incubusss@mandriva.org> 2.3.5-6mdv2010.0
+ Revision: 376681
- fix desktop file (#50170)
- fix license (GPLv2)

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 2.3.5-5mdv2009.1
+ Revision: 325277
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.3.5-4mdv2009.0
+ Revision: 246161
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.3.5-2mdv2008.1
+ Revision: 131676
+ rebuild (emptylog)

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.3.5-1mdv2008.1
+ Revision: 131563
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request

  + Austin Acton <austin@mandriva.org>
    - fix lib64 build
    - new version
    - Import gjots2



* Thu Mar 23 2006 Austin Acton <austin@mandriva.org> 2.3.4-2mdk
- use python install
- cleanup spec

* Sun Mar 05 2006 Austin Acton <austin@mandriva.org> 2.3.4-1mdk
- New release 2.3.4

* Tue Jan 24 2006 Lenny Cartier <lenny@mandriva.com> 2.3.3-1mdk
- 2.3.3

* Wed Jan 04 2006 Austin Acton <austin@mandriva.org> 2.3.0-1mdk
- New release 2.3.0

* Mon Dec 26 2005 Lenny Cartier <lenny@mandriva.com> 2.2.1-1mdk
- 2.2.1

* Tue Nov 8 2005 Austin Acton <austin@mandriva.org> 2.2.0-3mdk
- requires gnomevfs wrapper
- Eskild is my overlord

* Sat Sep 10 2005 Austin Acton <austin@mandriva.org> 2.2.0-2mdk
- more missing files

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 2.2.0-1mdk
- New release 2.2.0

* Sat Mar 19 2005 Austin Acton <austin@mandrake.org> 2.1.1-1mdk
- 2.1.1
- add missing files

* Thu Nov 11 2004 Austin Acton <austin@mandrake.org> 2.0.1-1mdk
- 2.0.1
- pretty transparent icon

* Thu May 27 2004 Abel Cheung <deaddog@deaddog.org> 2.0.0-1mdk
- First Mandrake package
