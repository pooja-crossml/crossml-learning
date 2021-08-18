# from django.test import TestCase
# from .models import candidate_data

# # class BasicTest(TestCase):
	
# #     def setUp(self):
# #         print('setup is called')
	
# #     def test_me(self):
# #         print("test case running")

# #     def tearDown(self):
# #         print("Teardown called")

# class CandidateData(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         candidate_data.objects.create(candidate_name = "Marry", resume_portfolio_link="http://marry@virtual.com", primary_skills="python", secondary_skills="javascript",candidate_experince=2 )
              
#     def test_cadidate_data(self):
#         candidate = candidate_data.objects.get(id=1)
#         candidate_name = candidate._meta.get_field('candidate_name').verbose_name
#         self.assertTrue(candidate_name).verbose_name


#         # Author.objects.create(first_name='Big', last_name='Bob')

#         # author = Author.objects.get(id=1)
#         # field_label = author._meta.get_field('first_name').verbose_name
#         # self.assertEqual(field_label, 'first name')