package org.hinex.alpha.facepp;

import static org.junit.Assert.*;

import java.nio.charset.Charset;

import org.hinex.alpha.util.TestResource;
import org.json.JSONObject;

import com.facepp.http.HttpRequests;
import com.facepp.http.PostParameters;

class Test {

	@org.junit.Test
	public void test() {
		HttpRequests httpRequests = new HttpRequests("4480afa9b8b364e30ba03819f3e9eff5", "Pz9VFT8AP3g_Pz8_dz84cRY_bz8_Pz8M ", true, true);
		
		JSONObject result = null;
		
		result = httpRequests.detectionDetect(new PostParameters().setImg(TestResource.getFile('hx_pj.JPG')))
		println result.getJSONArray('face').getJSONObject(0).getString('face_id')
		fail("Not yet implemented");
	}

}
