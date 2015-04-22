/* 
 * @author Hinex
 * @date 2015-4-13 16:08:05
 */

package org.hinex.alpha.trunk.javassist.reflect;

public class Entity {
	
	private String field1;

	public String getField1() {
		System.out.println("msg from entity: invoke getField1 method");
		return field1;
	}
	
	public void setField1(String field1) {
		System.out.println("msg from entity: invoke setField1 method");
		this.field1 = field1;
	}

}
