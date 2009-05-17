%define name	gjots2
%define version 2.3.5
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A note jotter in tree structure
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://bhepple.freeshell.org/gjots/
Source:		http://bhepple.freeshell.org/gjots/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	pygtk2.0-libglade >= 2.2.0
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
