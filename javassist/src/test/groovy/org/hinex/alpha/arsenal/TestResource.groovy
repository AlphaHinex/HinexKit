package org.hinex.alpha.arsenal

class TestResource {
	
	static File getFile(String fileName) {
		new File("${new File('').getAbsolutePath()}/src/test/resources/$fileName")
	}

}
