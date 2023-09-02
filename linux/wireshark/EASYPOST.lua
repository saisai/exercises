-- EASYPOST.lua
-- Replace occurrences of "easypost/EASYPOST" with protocol/dissector name.
-- Grab and format fields as needed

-- Step 1 - document as you go. See header above and set_plugin_info().
local easypost_info =
{
    version = "1.0.0",
    author = "Good Coder",
    description = "Important EASYPOST stuff",
    repository = "Floppy in top drawer"
}

set_plugin_info(easypost_info)

-- Step 2 - create a protocol to attach new fields to
local easypost_p = Proto.new("easypost","Important EASYPOST Protocol")

-- Step 3 - add some field(s) to Step 2 protocol
local pf = { payload = ProtoField.string("easypost.payload", "EASYPOST data") }

easypost_p.fields = pf

-- Step 4 - create a Field extractor to copy packet field data.
easypost_payload_f = Field.new("frame.protocols")

-- Step 5 - create the postdissector function that will run on each frame/packet
function easypost_p.dissector(tvb,pinfo,tree)
    local subtree = nil

    -- copy existing field(s) into table for processing
    finfo = { easypost_payload_f() }

    if (#finfo > 0) then
        if not subtree then
            subtree = tree:add(easypost_p)
        end
        for k, v in pairs(finfo) do
            -- process data and add results to the tree
	        local field_data = string.format("%s", v):upper()
	        subtree:add(pf.payload, field_data)
        end
    end
end

-- Step 6 - register the new protocol as a postdissector
register_postdissector(easypost_p)
