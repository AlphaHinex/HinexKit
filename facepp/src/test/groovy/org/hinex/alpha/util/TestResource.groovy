package org.hinex.alpha.util

class TestResource {
	
	static File getFile(name) {
		new File("${new File('').getAbsolutePath()}/src/test/resources/$name")
	}
	
}
