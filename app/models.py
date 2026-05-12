from typing import List, Optional

from pydantic import BaseModel, Field


class GapInput(BaseModel):
    name: str
    priority: str = "Medium"
    match: str = ""


class CourseInput(BaseModel):
    courseId: str
    title: str
    url: str
    provider: str
    providerDetail: str = ""
    description: str = ""
    targetSkill: str = ""
    relevanceScore: float = 0.5
    xp: int = 40


class SyncAnalysisRequest(BaseModel):
    resumeId: str
    resumeLabel: str
    analysisId: str
    matchPercent: int = Field(ge=0, le=100)
    gaps: List[GapInput]
    jobDescription: Optional[str] = ""
    courses: Optional[List[CourseInput]] = None


class RefreshRecommendationsRequest(BaseModel):
    resumeId: str
    analysisId: str


class CompleteCourseRequest(BaseModel):
    resumeId: str
    analysisId: str


class CourseProgress(BaseModel):
    courseId: str
    title: str
    url: str
    provider: str
    providerDetail: str
    description: str
    targetSkill: str
    relevanceScore: float
    xp: int
    position: int
    status: str
    completedAt: Optional[str] = None


class Achievement(BaseModel):
    id: str
    title: str
    description: str
    unlocked: bool


class Activity(BaseModel):
    courseId: str
    title: str
    xp: int
    completedAt: str
    resumeLabel: str


class ProgressResponse(BaseModel):
    userId: str
    resumeId: str
    resumeLabel: str
    analysisId: str
    matchPercent: int
    earnedXp: int
    baseXp: int
    totalXp: int
    level: int
    nextLevelXp: int
    courses: List[CourseProgress]
    achievements: List[Achievement]
    recentActivity: List[Activity]
    currentStreak: int = 0
