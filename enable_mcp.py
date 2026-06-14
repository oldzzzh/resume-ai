"""Enable BlenderMCP addon and start MCP server"""
import bpy

# Enable the addon
bpy.ops.preferences.addon_enable(module="blender_mcp_addon")
bpy.ops.wm.save_userpref()

# Start the MCP server by running the addon's operator
bpy.ops.blendermcp.start_server()

print("BlenderMCP server started!")
