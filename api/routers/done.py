from fastapi import APIRouter

router = APIRouter()

# @router.get('test')
# async def test():
#     pass

@router.put('task/{task_id}/done')
async def mark_task_sd_done():
    pass

@router.delete('task?{task_id}/done')
async def unmark_task_as_done():
    pass