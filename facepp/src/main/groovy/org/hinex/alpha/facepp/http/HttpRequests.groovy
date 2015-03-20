/* 
 * @author Hinex
 * @date 2015-3-20 9:06:20
 */

package org.hinex.alpha.facepp.http

import java.net.Proxy;

import org.json.JSONObject

import com.facepp.error.FaceppParseException
import com.facepp.http.PostParameters

class HttpRequests extends com.facepp.http.HttpRequests {
	
	public HttpRequests() {
		super()
	}
	
	public HttpRequests(String apiKey, String apiSecret, boolean isCN, boolean isDebug) {
		this();
		this.apiKey = apiKey;
		this.apiSecret = apiSecret;
		setWebSite(isCN, isDebug);
	}
	
	public JSONObject detectionDetect(PostParameters params, Proxy proxy, String auth) throws FaceppParseException{
		return request("detection", "detect", params, proxy, auth);
	}

}
