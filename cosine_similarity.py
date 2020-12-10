from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_matches(ads, user):
  corpus = [user, *[item["content"] for item in ads]]
  vectorizer = CountVectorizer()
  X = vectorizer.fit_transform(corpus)
  # print(vectorizer.get_feature_names()) 
  cosine_sim = cosine_similarity(X) 
  matches = cosine_sim[0][1:]
  max_index = matches.argmax() 
  return ads[max_index] 