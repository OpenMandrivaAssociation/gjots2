Name:		gjots2
Version:	2.4.1
Release:	1
Summary:	A note jotter in tree structure
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://bhepple.freeshell.org/gjots/
Source:		http://bhepple.freeshell.org/gjots/%{name}-%{version}.tgz
BuildArch:	noarch
Requires:	pygtk2.0
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
python setup.py install --root=%{buildroot}
%find_lang %{name}

# fix desktop file
sed -i -e 's/gjots.png/gjots/' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
	--remove-key=Encoding \
	--remove-category=Application \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

# icons
install -d -m 755 %{buildroot}%{_liconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
convert -geometry 48x48 pixmaps/gjots.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 pixmaps/gjots.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 pixmaps/gjots.png %{buildroot}%{_miconsdir}/%{name}.png

%files -f %{name}.lang
%doc %{_docdir}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{py_puresitedir}/*
%{_prefix}/lib/%{name}
%{_mandir}/man1/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

