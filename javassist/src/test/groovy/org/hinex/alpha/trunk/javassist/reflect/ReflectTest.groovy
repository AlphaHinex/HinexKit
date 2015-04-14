/* 
 * @author Hinex
 * @date 2015-4-13 15:13:49
 */

package org.hinex.alpha.trunk.javassist.reflect;

import static org.hamcrest.core.IsEqual.*
import static org.junit.Assert.*
import javassist.ClassPool
import javassist.CtClass
import javassist.CtField
import javassist.bytecode.AccessFlag
import javassist.bytecode.ClassFile
import javassist.bytecode.FieldInfo

import org.hinex.alpha.arsenal.TestResource
import org.junit.Before
import org.junit.Test

class ReflectTest {
	
	private static final String FIELD1 = 'field1'
	
	private static final String VALUE1 = 'value1'
	
	private static final String ENTITY = 'org.hinex.alpha.trunk.javassist.reflect.Entity'
	
	private ClassPool pool
	
	private CtClass cc
	
	private ProxyClassLoader loader
	
	@Before
	public void setUp() {
		pool = ClassPool.getDefault()
		cc = pool.get(ENTITY)
		loader = new ProxyClassLoader(this.class.classLoader)
	}
	
	@Test(expected = NoSuchFieldException.class)
	public void couldNotSetPrivateFieldValue() {
		Class clz = Entity.class
		Entity inst = clz.newInstance()
		clz.getField(FIELD1).set(inst, VALUE1)
	}
	
	@Test
	public void couldSetPrivateFieldAfterModifyAccessFlags() {
		CtField cf = cc.getField(FIELD1)
		FieldInfo fieldInfo = cf.fieldInfo 
		assertThat fieldInfo.getAccessFlags(), equalTo(AccessFlag.PRIVATE)
		
		fieldInfo.setAccessFlags(AccessFlag.PUBLIC)
		Class clz = cc.toClass(loader, null)
		Object proxy = clz.newInstance()
		clz.getField(FIELD1).set(proxy, VALUE1)
		assertThat clz.getField(FIELD1).get(proxy), equalTo(VALUE1)
		
		println "no message from entity before\n${'-'*10}"
		
		println "this operation will invoke Entity's method"
		assertThat proxy.getField1(), equalTo(VALUE1)
	}
	
}
