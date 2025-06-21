#!/usr/bin/env python3
"""
Enhanced Real Estate Automation System Test
테스트: 향상된 부동산 자동화 시스템
"""

import sys
import os
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_system_initialization():
    """시스템 초기화 테스트"""
    try:
        logger.info("🧪 Enhanced automation system initialization test starting...")
        
        from complete_automation import CompleteAutomationSystem
        
        system = CompleteAutomationSystem()
        logger.info("✅ CompleteAutomationSystem initialized successfully")
        
        components_to_check = [
            ('property_lookup', 'PropertyLookupManager'),
            ('weekly_schedule', 'WeeklyScheduleManager'),
            ('ten_manager', 'TENWebsiteManager'),
            ('serve_manager', 'ServeWebsiteManager')
        ]
        
        for attr_name, component_name in components_to_check:
            if hasattr(system, attr_name):
                logger.info(f"✅ {component_name} component loaded")
            else:
                logger.error(f"❌ {component_name} component missing")
                return False
        
        workflow_methods = [
            'start_weekly_automation',
            'create_qa_video_workflow', 
            'register_on_all_platforms',
            'enhanced_automation_workflow'
        ]
        
        for method_name in workflow_methods:
            if hasattr(system, method_name):
                logger.info(f"✅ {method_name} method available")
            else:
                logger.error(f"❌ {method_name} method missing")
                return False
        
        logger.info("🎯 System initialization test completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"❌ System initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_property_lookup_functionality():
    """부동산 조회 기능 테스트"""
    try:
        logger.info("🏢 Testing property lookup functionality...")
        
        from complete_automation import PropertyLookupManager
        
        lookup_manager = PropertyLookupManager()
        
        logger.info("📋 Testing Friday Folder CSV check...")
        friday_apartments = lookup_manager.check_friday_folder_csv()
        logger.info(f"Friday Folder result: {len(friday_apartments)} apartments found")
        
        logger.info("🗺️ Testing Naver Map API integration...")
        nearby_apartments = lookup_manager.find_nearby_apartments_naver("강남구")
        logger.info(f"Naver Map result: {len(nearby_apartments)} apartments found")
        
        logger.info("🎯 Testing property data for automation...")
        property_info = lookup_manager.get_property_for_automation("서울시 강남구")
        logger.info(f"Property info: {property_info}")
        
        logger.info("✅ Property lookup functionality test completed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Property lookup test failed: {e}")
        return False

def test_weekly_schedule_functionality():
    """주간 스케줄링 기능 테스트"""
    try:
        logger.info("📅 Testing weekly schedule functionality...")
        
        from complete_automation import WeeklyScheduleManager, CompleteAutomationSystem
        
        system = CompleteAutomationSystem()
        schedule_manager = WeeklyScheduleManager(system)
        
        logger.info("⏰ Testing weekly schedule setup...")
        setup_result = schedule_manager.setup_weekly_schedule()
        logger.info(f"Schedule setup result: {setup_result}")
        
        logger.info("❓ Testing Q&A script creation...")
        qa_script = schedule_manager._create_qa_script({
            'name': '테스트 아파트',
            'address': '서울시 강남구 대치동',
            'type': '아파트'
        })
        logger.info(f"Q&A script created: {len(qa_script)} pairs")
        
        logger.info("✅ Weekly schedule functionality test completed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Weekly schedule test failed: {e}")
        return False

def test_qa_voice_generation():
    """Q&A 음성 생성 테스트"""
    try:
        logger.info("🎙️ Testing Q&A voice generation...")
        
        from complete_automation import RealTTSEngine
        
        tts_engine = RealTTSEngine()
        
        qa_pairs = [
            {
                'question': '이 아파트의 특징은 무엇인가요?',
                'answer': '교통이 편리하고 주변 시설이 잘 갖춰져 있습니다.'
            }
        ]
        
        output_folder = "/tmp/test_voices"
        os.makedirs(output_folder, exist_ok=True)
        
        voice_files = tts_engine.generate_qa_voices(qa_pairs, output_folder)
        logger.info(f"Generated voice files: {len(voice_files)}")
        
        logger.info("✅ Q&A voice generation test completed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Q&A voice generation test failed: {e}")
        return False

def main():
    """메인 테스트 실행"""
    logger.info("🚀 Starting Enhanced Real Estate Automation System Tests")
    logger.info("=" * 60)
    
    tests = [
        ("System Initialization", test_system_initialization),
        ("Property Lookup Functionality", test_property_lookup_functionality),
        ("Weekly Schedule Functionality", test_weekly_schedule_functionality),
        ("Q&A Voice Generation", test_qa_voice_generation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        logger.info(f"\n🧪 Running test: {test_name}")
        logger.info("-" * 40)
        
        try:
            if test_func():
                logger.info(f"✅ {test_name} PASSED")
                passed += 1
            else:
                logger.error(f"❌ {test_name} FAILED")
        except Exception as e:
            logger.error(f"❌ {test_name} FAILED with exception: {e}")
    
    logger.info("\n" + "=" * 60)
    logger.info(f"🎯 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        logger.info("🎉 All tests passed! Enhanced system is ready.")
        return True
    else:
        logger.error(f"⚠️ {total - passed} tests failed. Please check the issues.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
