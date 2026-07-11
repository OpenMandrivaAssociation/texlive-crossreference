%global tl_name crossreference
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Crossreferences within documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/crossreference
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines cross-references (essentially 'grand' label
references), which may be listed in a table of cross-references.

