if not quarto.doc or not quarto.doc.is_format("pdf") then
  return {}
end

local function formatted_now()
  return os.date("%B %e, %Y")
end

function Meta(meta)
  local last_modified = formatted_now()
  meta.title = pandoc.MetaString("FLIM Playground Manual")
  meta["title-meta"] = pandoc.MetaString("FLIM Playground Manual")
  meta.author = pandoc.MetaList({})
  meta["author-meta"] = pandoc.MetaList({})
  meta.date = pandoc.MetaString(last_modified)
  meta["date-meta"] = pandoc.MetaString(last_modified)
  return meta
end
