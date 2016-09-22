# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

from GlyphsApp.plugins import *

class showMetricsOnTypeTool(ReporterPlugin):

	def settings(self):
		self.menuName = 'Metrics On Type Tool'

	def foreground(self, layer):
		font = Glyphs.font
		layer = font.selectedLayers[0]

		scale = self.getScale()
		NSBezierPath.setDefaultLineWidth_( 1.0/scale )
		NSColor.darkGrayColor().set

		rp = layer.width
		dp = font.selectedFontMaster.descender
		ap = font.selectedFontMaster.ascender

		ls = NSPoint( 0, dp )
		le = NSPoint( 0, ap )
		NSBezierPath.strokeLineFromPoint_toPoint_( ls, le )

		rs = NSPoint( rp, dp )
		re = NSPoint( rp, ap )
		NSBezierPath.strokeLineFromPoint_toPoint_( rs, re )

	# def needsExtraMainOutlineDrawingForInactiveLayer_(self, layer):
	# 	return True
	#
	# def inactiveLayers(self, layer):
	# 	font = Glyphs.font
	# 	layer = font.selectedLayers[0]
	#
	# 	scale = self.getScale()
	# 	NSBezierPath.setDefaultLineWidth_( 1.0/scale )
	# 	NSColor.redColor().set
	#
	# 	rp = layer.width
	# 	dp = font.selectedFontMaster.descender
	# 	ap = font.selectedFontMaster.ascender
	#
	# 	ls = NSPoint( 0, dp )
	# 	le = NSPoint( 0, ap )
	# 	NSBezierPath.strokeLineFromPoint_toPoint_( ls, le )
	#
	# 	rs = NSPoint( rp, dp )
	# 	re = NSPoint( rp, ap )
	# 	NSBezierPath.strokeLineFromPoint_toPoint_( rs, re )
