package org.hinex.alpha.facepp;

import static org.junit.Assert.*

import org.hinex.alpha.util.TestResource
import org.json.JSONObject
import org.junit.Before
import org.junit.Test

import com.facepp.http.HttpRequests
import com.facepp.http.PostParameters

class FaceppTest {
	
	HttpRequests httpRequests
	
	@Before
	public void setUp() {
		def apiKey = '9b851bc50ac8f084f36fd4d932886946'
		def apiSecret = 'kN1tZJcAjaVEyNqq2XZX2gZhuZNLijcS'
		httpRequests = new HttpRequests(apiKey,  apiSecret, true, true);
	}
	
	@Test
	public void createGroup() {
		println httpRequests.groupCreate(new PostParameters().setGroupName('Demo Group'))
	}
	
	@Test
	public void createPerson() {
		println httpRequests.personCreate(new PostParameters().setPersonName('hinex'))
	}
	
	@Test
	public void addPersonToGroup() {
		println httpRequests.groupAddPerson(new PostParameters().setGroupName('Demo Group').setPersonName('hinex'))
	}
	
	@Test
	public void addFaceToPerson() {
		JSONObject result = httpRequests.detectionDetect(new PostParameters().setImg(TestResource.getFile('hx_sd.JPG')))
		def faceId = result.getJSONArray('face').getJSONObject(0).getString('face_id')
		println httpRequests.personAddFace(new PostParameters().setPersonName('hinex').setFaceId(faceId))
	}
	
	@Test
	public void train() {
		def result = httpRequests.trainVerify(new PostParameters().setPersonName('hinex'))
		println result
		def sessionId = result.getString('session_id')
		println sessionId
		
		def resp
		while(true) {
			resp = httpRequests.infoGetSession(new PostParameters().setSessionId(sessionId))
			if('SUCC' == resp.getString('status')) {
				println 'success'
				println resp
				break
			} else {
				println resp.getString('status')
				println 'sleep 1s'
				sleep(1000)
			}
		}
	}
	
	@Test
	public void verify() {
		def result = httpRequests.detectionDetect(new PostParameters().setImg(TestResource.getFile('hx_mm.png')))
		def faceId = result.getJSONArray('face').getJSONObject(0).getString('face_id')
		println httpRequests.recognitionVerify(new PostParameters().setPersonName('hinex').setFaceId(faceId))
	}
	
	@Test
	public void compare() {
		def result1 = httpRequests.detectionDetect(new PostParameters().setImg(TestResource.getFile('hx_mm.png')))
		def faceId1 = result1.getJSONArray('face').getJSONObject(0).getString('face_id')
		
		def result2 = httpRequests.detectionDetect(new PostParameters().setImg(TestResource.getFile('hx_sd.JPG')))
		def faceId2 = result2.getJSONArray('face').getJSONObject(0).getString('face_id')
		
		println httpRequests.recognitionCompare(new PostParameters().setFaceId1(faceId1).setFaceId2(faceId2))
	}

}
