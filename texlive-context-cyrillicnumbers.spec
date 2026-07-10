%global tl_name context-cyrillicnumbers
%global tl_revision 47085

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Write numbers as cyrillic glyphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-cyrillicnumbers
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cyrillicnumbers.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cyrillicnumbers.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends ConTeXt's system of number conversion, by adding
numeration using cyrillic letters.

