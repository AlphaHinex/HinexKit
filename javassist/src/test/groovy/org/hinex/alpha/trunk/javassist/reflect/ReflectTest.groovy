/* 
 * @author Hinex
 * @date 2015-4-13 15:13:49
 */

package org.hinex.alpha.trunk.javassist.reflect;

import static org.hamcrest.core.IsEqual.*
import static org.junit.Assert.*

import java.lang.reflect.Field
import java.lang.reflect.Modifier;

import javassist.ClassPool
import javassist.CtClass
import javassist.CtField
import javassist.bytecode.AccessFlag
import javassist.bytecode.FieldInfo

import org.junit.Before
import org.junit.Test

class ReflectTest {
	
	private static final String FIELD1 = 'field1'
	
	private static final String VALUE1 = 'value1'
	
	private static final String ENTITY = 'org.hinex.alpha.trunk.javassist.reflect.Entity'
	
	private ClassPool pool
	
	private CtClass cc
	
	private ProxyClassLoader loader
	
	private Class clz
	
	private Entity inst
	
	@Before
	public void setUp() {
		pool = ClassPool.getDefault()
		cc = pool.get(ENTITY)
		loader = new ProxyClassLoader(this.class.classLoader)
		clz = Entity.class
		inst = clz.newInstance()
	}
	
	@Test(expected = NoSuchFieldException.class)
	public void couldNotDirectlyGetPrivateField() {
		clz.getField(FIELD1)
	}
	
	@Test(expected = IllegalAccessException.class)
	public void couldGetPrivateFieldButNotSetDirectly() {
		Field field = clz.getDeclaredField(FIELD1)
		field.set(inst, VALUE1)
	}
	
	@Test
	public void couldSetPrivateFieldAfterModifyAccessible() {
		Field field = clz.getDeclaredField(FIELD1)
		assertThat field.getModifiers(), equalTo(Modifier.PRIVATE)
		
		field.setAccessible(true)
		assertThat field.getModifiers(), equalTo(Modifier.PRIVATE)
		
		field.set(inst, VALUE1)
		assertThat field.get(inst), equalTo(VALUE1)
	}
	
	@Test
	public void couldSetPrivateFieldUsingProxy() {
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
