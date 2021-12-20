## 配置外部搜索引擎

*LookUp engine*

打开配置文件：Edit -> Preferences -> Advanced -> Files and Folders -> Data Directory Location -> Show Data Directory -> locate文件夹 -> engines.json

作用：**一键查找**，根据所选条目(item)的信息（论文名，期刊等），**直接打开**一些学术网站（谷歌学术，期刊查询等）的**查询结果**

搜索模板配置：

- 论文名：`{z:title}`
- 期刊名：`{rft:jtitle}` (ref: [How to search "publication" in Zotero LookUp engine?](https://forums.zotero.org/discussion/81749/how-to-search-publication-in-zotero-lookup-engine))

备份一下`engines.json`文件：

```json
[
	{
		"_name": "CrossRef Lookup",
		"_alias": "CrossRef",
		"_description": "CrossRef Search Engine",
		"_icon": "https://crossref.org/favicon.ico",
		"_hidden": false,
		"_urlTemplate": "https://crossref.org/openurl?{z:openURL}&pid=zter:zter321",
		"_urlParams": [],
		"_urlNamespaces": {
			"z": "http://www.zotero.org/namespaces/openSearch#",
			"": "http://a9.com/-/spec/opensearch/1.1/"
		},
		"_iconSourceURI": "https://crossref.org/favicon.ico"
	},
	{
		"_name": "Google Scholar Search",
		"_alias": "Google Scholar",
		"_description": "Google Scholar Search",
		"_icon": "https://scholar.google.com/favicon.ico",
		"_hidden": false,
		"_urlTemplate": "https://scholar.google.com/scholar?as_q=&as_epq={z:title}&as_occt=title&as_sauthors={rft:aufirst?}+{rft:aulast?}&as_ylo={z:year?}&as_yhi={z:year?}&as_sdt=1.&as_sdtp=on&as_sdtf=&as_sdts=22&",
		"_urlParams": [],
		"_urlNamespaces": {
			"rft": "info:ofi/fmt:kev:mtx:journal",
			"z": "http://www.zotero.org/namespaces/openSearch#",
			"": "http://a9.com/-/spec/opensearch/1.1/"
		},
		"_iconSourceURI": "https://scholar.google.com/favicon.ico"
	},
	{
		"_name": "Connected Papers",
		"_alias": "Connected Papers文献网络",
		"_description": "Connected Papers文献网络",
		"_icon": "https://www.connectedpapers.com/favicon.ico",
		"_hidden": false,
		"_urlTemplate": "https://www.connectedpapers.com/search?q={z:title}+{z:year}",
		"_urlParams": [],
		"_urlNamespaces": {
			"rft": "info:ofi/fmt:kev:mtx:journal",
			"z": "http://www.zotero.org/namespaces/openSearch#",
			"": "http://a9.com/-/spec/opensearch/1.1/"
		},
		"_iconSourceURI": "https://www.connectedpapers.com/favicon.ico"
	},
	{
		"_name": "Sci-Hub DOI",
		"_alias": "Sci-Hub DOI",
		"_description": "SciHub Lookup",
		"_icon": "http://sci-hub.se/favicon.ico",
		"_hidden": false,
		"_urlTemplate": "http://sci-hub.ee/{z:DOI}",
		"_urlParams": [],
		"_urlNamespaces": {
			"z": "http://www.zotero.org/namespaces/openSearch#"
		},
		"_iconSourceURI": "http://sci-hub.se/favicon.ico"
	},
	{
		"_name": "iJournal",
		"_alias": "iJournal",
		"_description": "iJournal Lookup",
		"_icon": "https://ijournal.topeditsci.com/favicon.ico",
		"_hidden": false,
		"_urlTemplate": "https://ijournal.topeditsci.com/search?keywordType=title&keyword={rft:jtitle}",
		"_urlParams": [],
		"_urlNamespaces": {
			"rft": "info:ofi/fmt:kev:mtx:journal",
			"z": "http://www.zotero.org/namespaces/openSearch#"
		},
		"_iconSourceURI": "https://ijournal.topeditsci.com/favicon.ico"
	}
]
```