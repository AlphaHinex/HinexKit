/* 
 * @author Hinex
 * @date 2015-4-13下午3:13:49
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
	
	private ClassLoader loader
	
	@Before
	public void setUp() {
		pool = ClassPool.getDefault()
		cc = pool.get(ENTITY)
		loader = this.class.classLoader
	}
	
	@Test(expected = NoSuchFieldException.class)
	public void couldNotSetPrivateFieldValue() {
		Class clz = loader.loadClass(ENTITY)
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
		Entity inst = clz.newInstance()
		clz.getField(FIELD1).set(inst, VALUE1)
		assertThat inst.getField1(), equalTo(VALUE1)
	}
	
//	@Test
//	public void readClass() {
//		def fin = new BufferedInputStream(new FileInputStream(TestResource.getFile('Document.class')))
//		ClassFile cf = new ClassFile(new DataInputStream(fin))
//		cf.fields.each {
//			println it
//		}
//	}
//
//	@Test
//	public void test() {
//		ClassPool pool = ClassPool.getDefault()
//		CtClass cc = pool.get('org.hinex.alpha.trunk.javassist.reflect.Entity')
//		cc.getProperties().each {
//			println "property: $it"
//		}
//		cc.getFields().each {
//			println "ctfield: $it"
//		}
//		Class clz = cc.toClass()
//		Entity inst = clz.newInstance()
//		clz.getFields().each {
//			println "field: $it"
//		}
//		clz.getField('field1').set(inst, '123')
//		println inst.getField1()
//	}

}
